
we will take your software skills to the next level by focusing on the specifics needed to move code into a production setting.

These specifics will focus on:

* Handling errors
* Writing tests and logs
* Model drift
* Automated vs. non-automated retraining

With these skills in your toolkit, you will be ready to take on the project for this course, as well as contribute to your team's production codebase!


# Catching Errors

you saw how to use try/ except blocks in order to catch errors. There are actually a lot of different considerations to errors, so if you would like to learn more, the link below provides some additional resources.


Catching errors in Python code is essential for writing robust and reliable applications. One common method for handling errors is using try-except blocks, which allow you to catch exceptions that occur during the execution of your code and handle them gracefully.

```python
try:

    result = 10 / 0  # Attempting division by zero

except ZeroDivisionError as e:

    print("Error:", e)

    result = None
```

In this example, a ZeroDivisionError is raised when attempting to divide by zero. By wrapping the problematic code within a try block and specifying the exception type to catch in the except block, we can gracefully handle the error and prevent it from crashing the program.


Additionally, you can use the else block in combination with try-except to execute code only if no exceptions are raised.

```python
try:

    result = int(input("Enter a number: "))

except ValueError:

    print("Invalid input. Please enter a valid integer.")

else:

    print("You entered:", result)
```

Here, the code attempts to convert user input to an integer. If successful, the input is printed; otherwise, a ValueError is caught, and an error message is displayed.


Furthermore, you can utilize the finally block to execute cleanup code, regardless of whether an exception occurs or not.

```python
try:

    file = open("example.txt", "r")

    content = file.read()

except FileNotFoundError:

    print("File not found.")

else:

    print("File content:", content)

finally:

    if file:

        file.close()  # Ensuring file is closed even if an exception occurs
```

In this snippet, the file is opened for reading, and its content is displayed. If the file is not found, a FileNotFoundError is caught. Regardless of the outcome, the file is closed in the finally block to ensure proper resource management.


Handling errors effectively in Python enhances the reliability and maintainability of your codebase. By employing try-except blocks, you can anticipate and gracefully handle exceptions, ensuring smooth execution of your programs even in the face of unexpected issues.

https://docs.python.org/3/tutorial/errors.html


# Tests

Testing your code is essential before deployment. It helps you catch errors and faulty conclusions before they make any major impact. Today, employers are looking for data scientists with the skills to properly prepare their code for an industry setting, which includes testing their code.

## Testing and data science

Problems that could occur in data science aren’t always easily detectable; you might have values being encoded incorrectly, features being used inappropriately, or unexpected data breaking assumptions.
To catch these errors, you have to check for the quality and accuracy of your analysis in addition to the quality of your code. Proper testing is necessary to avoid unexpected surprises and have confidence in your results.
Test-driven development (TDD): A development process in which you write tests for tasks before you even write the code to implement those tasks.
Unit test: A type of test that covers a “unit” of code—usually a single function—independently from the rest of the program.

Resources
* Four Ways Data Science Goes Wrong and How Test-Driven Data Analysis Can Help: Blog Post(opens in a new tab): https://www.predictiveanalyticsworld.com/machinelearningtimes/four-ways-data-science-goes-wrong-and-how-test-driven-data-analysis-can-help/6947/
* Ned Batchelder: Getting Started Testing: Slide Deck(opens in a new tab) and Presentation Video: https://speakerdeck.com/pycon2014/getting-started-testing-by-ned-batchelder, https://www.youtube.com/watch?v=FxSsnHeWQBY

## Unit Tests

We want to test our functions in a way that is repeatable and automated. Ideally, we'd run a test program that runs all our unit tests and cleanly lets us know which ones failed and which ones succeeded. Fortunately, there are great tools available in Python that we can use to create effective unit tests!

Unit Testing: Advantages and Disadvantages
The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved. They don't require access to databases, APIs, or other external sources of information. However, passing unit tests isn’t always enough to prove that our program is working successfully. To show that all the parts of our program work with each other properly, communicating and transferring data between them correctly, we use integration tests. In this lesson, we'll focus on unit tests; however, when you start building larger programs, you will want to use integration tests as well.

To learn more about integration testing and how integration tests relate to unit tests, see Integration Testing(opens in a new tab). That article contains other very useful links as well.
https://www.fullstackpython.com/integration-testing.html

## Unit Tests Tools

To install `pytest`, run `pip install -U pytest` in your terminal. You can see more information on getting started here(opens in a new tab). https://docs.pytest.org/en/latest/getting-started.html

* Create a test file starting with test_.
* Define unit test functions that start with `test_` inside the test file.
* Enter `pytest` into your terminal in the directory of your test file and it detects these tests for you.

`test_` is the default; if you wish to change this, you can learn how in this `pytest` configuration(opens in a new tab). https://docs.pytest.org/en/latest/example/pythoncollection.html

In the test output, periods represent successful unit tests and Fs represent failed unit tests. Since all you see is which test functions failed, it's wise to have only one assert statement per test. Otherwise, you won't know exactly how many tests failed or which tests failed.

Your test won't be stopped by failed assert statements, but it will stop if you have syntax errors.

Launching tests for ML models in production settings will be covered in more detail throughout this lesson, as well as in the project. However, it is also often done using cloud-based software; some additional resources can be found here on testing using Google's cloud-based systems(opens in a new tab). https://developers.google.com/machine-learning/testing-debugging/pipeline/deploying?hl=es-419


## Using Pytest Fixtures for Parameterized Tests
Pytest Fixtures are special functions that come into the picture when you need to:

Either write a parameterized test method, meaning you want to pass some arguments to the test method.
Or reuse a block of code in multiple test methods.
We define a Fixture using `@pytest.fixture` decorator ahead of the (non-test) function we want to repurpose in the test methods, as shown in the example below:

```{python}
# File: test_mylibrary.py
# Pytest filename starts with "test_...."
import pytest
import pandas as pd

##################################
"""
Function to test
"""
def import_data(pth):
    df = pd.read_csv(pth)
    return df
##################################
"""
Fixture - The test function test_import_data() will 
use the return of path() as an argument
"""
@pytest.fixture(scope="module")
def path():
    return "./data/bank_data.csv"

##################################
"""
Test method
"""
def test_import_data(path):
    try:
        df = import_data(path)

    except FileNotFoundError as err:
        logging.error("File not found")
        raise err

    # Check the df shape
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err
    return df
##################################
```

Run the test_mylibrary.py file above using the `pytest` command in your terminal.

In the example above,

* The path() fixture function is being used as an argument to the test_import_data() method.
* The path() fixture function has `scope="module"`. You can share fixtures across classes, modules, packages or session.

The fixture function is reusable, meaning you can use it in multiple test functions. Note that fixture functions are not meant to be called directly, but are used automatically when test methods request them as parameters.

Moreover, you can define setup/teardown statements in the fixture function that you may want to use in multiple test functions.

Note that Fixtures can request other fixtures, and there are plenty of built-in Pytest fixtures available.

### Additional Resource
* How to use fixtures(opens in a new tab). https://docs.pytest.org/en/7.1.x/how-to/fixtures.html

* Parametrizing fixtures(opens in a new tab). https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#fixture-parametrize - Read this section to understand how you can pass parameters to the fixture functions using the built-in request object. In such cases, we use the fixture decorator as:

`@pytest.fixture(scope="module", params=["argument1", "argument2"])`

The params list contains a list of values for each of which the fixture function will execute. You can access the parameters list later inside the fixture function as:

`value = request.param`

For example, see a fixture below that will execute for each parameter:

```{python}
@pytest.fixture(scope="module", params=["./data/bank_data.csv", "./data/hospital_data.csv"])
def path():
  value = request.param
  return value
```

### Additional Resources:

Effective Python Testing With Pytest. https://realpython.com/pytest-python-testing/: This comprehensive tutorial on Real Python covers intermediate and advanced pytest features, including fixtures, marks, parameters, and plugins.
Testing using Pytest(opens in a new tab)

Mocking External APIs in Python: Integrating with third-party applications extends your product's functionality, but it also presents challenges. This tutorial provides insights into handling external APIs effectively.
Pytests and Mocks(opens in a new tab). https://realpython.com/testing-third-party-apis-with-mocks/

A Gentle Introduction to Testing with PyTest: Understand the basics of writing tests, formalizing requirements as code, and leveraging pytest's features.
Pytest. https://bas.codes/posts/python-pytest-introduction/

## Passing Values Across Test Functions
In some cases, you may want to test a series of functions dependent on each other, meaning the return of one function is used as an argument to the other function.

In such cases, you can store your test cases' results either in the Pytest Namespace or Cache.

### Method 1: Using Namespace
Before we dive in, let's understand about conftest.py file..

'''
The conftest.py(opens in a new tab) https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files file serves as a means of providing fixtures for an entire directory. Any test can use fixtures defined in a conftest.py in that package
'''

In summary, the Pytest looks for a conftest.py file when:

* Tests from multiple test modules want to access the fixture functions
* You want to define Pytest configurations, such as storing variables in the Namespace.

Let's see an example where you'd want to store a Dataframe from one test function and access it later in another test function.

* The example below uses the Namespace to store and access the Dataframe object.

```{python}
# conftest.py
import pytest
def df_plugin():
    return None
# Creating a Dataframe object 'pytest.df' in Namespace
def pytest_configure():
    pytest.df = df_plugin()
```

Once you have the conftest.py above ready, you can access and redefine `pytest.df` in test functions as:

```{python}
# Test function
# See the `pytest.df = df` statement to store the variable in Namespace
def test_import_data():
    try:
        df = import_data("./data/bank_data.csv")
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
 	'''
    Some assertion statements per your requirement.
    '''
    pytest.df = df
    return df
```

Next, you can access the Dataframe object in the test_function_two() as:

```{python}
# Test function
# See the `df = pytest.df` statement accessing the Dataframe object from Namespace
def test_function_two():
    df = pytest.df
    '''
    Some assertion statements per your requirement.
    '''
```

Useful link: In pytest, what is the use of conftest.py files?(opens in a new tab). https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files

### Method 2: Using Cache
Cache helps in saving time on repeated test runs, as well as sharing data between tests.

* The cache object is available via `request.config.cache.set()` or `request.config.cache.get()` fixture as:

```{python}
# Test function 
# It uses the built-in request fixture
def test_import_data(request):
    try:
        df = import_data("./data/bank_data.csv")
    except FileNotFoundError as err:
        logging.error("File not found")
        raise err
 	'''
    Some assertion statements per your requirement.
    '''
 
    request.config.cache.set('cache_df', df)
    return df
```

You can access the Dataframe object in the test_function_two() as:

```{python}
# Test function
def test_function_two(request):
    df = request.config.cache.get('cache_df', None)
    '''
    Some assertion statements per your requirement.
    '''
```

Reference: config.cache object. https://docs.pytest.org/en/6.2.x/cache.html#the-new-config-cache-object

# Test-Driven Development and Data Science

* Test-driven development: Writing tests before you write the code that’s being tested. Your test fails at first, and you know you’ve finished implementing a task when the test passes.
* Tests can check for different scenarios and edge cases before you even start to write your function. When start implementing your function, you can run the test to get immediate feedback on whether it works or not as you tweak your function.
* When refactoring or adding to your code, tests help you rest assured that the rest of your code didn't break while you were making those changes. Tests also helps ensure that your function behavior is repeatable, regardless of external parameters such as hardware and time.

Test-Driven Development (TDD) is a software development approach where developers write tests for their code before writing the actual implementation. This process typically involves three main steps: writing a test that defines the desired behavior of a function or module, running the test (which should fail initially since the code hasn't been implemented yet), and finally writing the code to make the test pass. TDD ensures that the code meets the specified requirements and remains functional even as it evolves.


In the context of Data Science using Python, TDD can be a valuable practice for ensuring the correctness and reliability of data processing and analysis pipelines, as well as machine learning models. By writing tests for data preprocessing steps, feature engineering, model training, and evaluation metrics, data scientists can validate the behavior of their code and catch potential errors early in the development process.


Let's consider an example of applying TDD in data preprocessing. Suppose we have a function `normalize_data` that is responsible for normalizing numerical features in a dataset. We can start by writing a test that defines the expected behavior of this function:


```{python}
import unittest

from my_module import normalize_data

class TestDataPreprocessing(unittest.TestCase):

    def test_normalize_data(self):

        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        expected_result = [[-1.22474487, -1.22474487, -1.22474487],

                           [ 0.        ,  0.        ,  0.        ],

                           [ 1.22474487,  1.22474487,  1.22474487]]

        self.assertEqual(normalize_data(data), expected_result)

if __name__ == '__main__':

    unittest.main()
```

Here, we define a test case `TestDataPreprocessing` with a single test method `test_normalize_data`. This method asserts that the output of the normalize_data function matches the expected result for a given input dataset.


Next, we implement the `normalize_data` function in `my_module.py`:


```{python}
import numpy as np

def normalize_data(data):

    data = np.array(data)

    mean = np.mean(data, axis=0)

    std = np.std(data, axis=0)

    normalized_data = (data - mean) / std

    return normalized_data.tolist()
```

After writing the test and implementing the function, we run the test suite. If the implementation is correct, all tests should pass. If any test fails, we need to revise our code until all tests pass, ensuring the correctness of the function.

By following a TDD approach in Data Science using Python, data scientists can maintain high code quality, reduce bugs, and enhance the reproducibility of their data analysis workflows.


* Data Science TDD(opens in a new tab) https://www.linkedin.com/pulse/data-science-test-driven-development-sam-savage/
* TDD is Essential for Good Data Science: Here's Why(opens in a new tab) https://medium.com/@karijdempsey/test-driven-development-is-essential-for-good-data-science-heres-why-db7975a03a44
* Testing Your Code(opens in a new tab) (general python TDD) http://docs.python-guide.org/en/latest/writing/tests/


# Logging

Logging is valuable for understanding the events that occur while running your program. For example, if you run your model overnight and the results the following morning are not what you expect, log messages can help you understand more about the context in those results occurred. Let's learn about the qualities that make a log message effective.

## Log Messages
Logging is the process of recording messages to describe events that have occurred while running your software. Let's take a look at a few examples, and learn tips for writing good log messages.

### Tip: Be professional and clear
Bad: Hmmm... this isn't working???
Bad: idk.... :(
Good: Couldn't parse file.

### Tip: Be concise and use normal capitalization
Bad: Start Product Recommendation Process
Bad: We have completed the steps necessary and will now proceed with the recommendation process for the records in our product database.
Good: Generating product recommendations.

### Tip: Choose the appropriate level for logging
Debug: Use this level for anything that happens in the program. Error: Use this level to record any error that occurs. Info: Use this level to record all actions that are user driven or system specific, such as regularly scheduled operations.

### Tip: Provide any useful information
Bad: Failed to read location data
Good: Failed to read location data: store_id 8324971


## Logging in Python

In this screencast, we saw how we could set up logging in our python scripts. Below is the same code as shown in the above video, which can be used as a template any time you need to set up logging for any of your situations.

```{python}
import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')
```

We also saw three common levels to be logged. These three levels are:

1. `info` 
2. `warning` 
3. `error`

Logging in Python is a crucial tool for understanding and troubleshooting the behavior of your applications. It allows you to record relevant information, such as error messages, warnings, and informational messages, to various outputs such as the console, files, or even external services.


```{python}
import logging


# Configure logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Example usage

def divide(x, y):

    try:

        result = x / y

    except ZeroDivisionError:

        logging.error("Division by zero occurred.")

        return None

    else:

        logging.info("Division successful. Result: %s", result)

        return result

# Test the function

result = divide(10, 2)
```

In this example, we import the logging module and configure it to log messages at the INFO level or above, with a specific format. We then define a function `divide` that attempts to divide two numbers. If a ZeroDivisionError occurs, an error message is logged. Otherwise, an informational message is logged with the result of the division.


You can customize the logging behavior further by specifying different levels of severity for messages, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.

```{python}
# Customizing logging levels

logging.basicConfig(level=logging.DEBUG)

def process_data(data):

    logging.debug("Processing data: %s", data)

    # Process data...
```

Here, we set the logging level to DEBUG, allowing us to log detailed debugging information within the `process_data` function. These debug messages will only be displayed if the logging level is set to DEBUG or lower.


Moreover, you can direct log messages to different destinations by adding handlers to the logger.


```{python}
# Adding a file handler

file_handler = logging.FileHandler('app.log')

file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Attach the handler to the logger

logger = logging.getLogger()

logger.addHandler(file_handler)

# Log an error message

logging.error("An error occurred. Check app.log for details.")
```

In this snippet, we create a file handler that logs messages with a severity level of ERROR or above to a file named `app.log`. We then attach the handler to the root logger so that any error messages logged will be written to the file.


By incorporating logging into your Python code, you can gain valuable insights into its execution and effectively diagnose issues, ultimately improving the reliability and maintainability of your applications.


## Testing & Logging

### Testing and Logging

In the two videos below, we will continue to look at the previous code example. However, we will look at the addition of `assert` statements as a way to to test our expectations within a function. We then will combine this with logging, as well as our `try/except` blocks.

In the previous video, we were introduced to `isinstance` as a way to check our data types, which is one of the most common checks we will want to do in any function.

Next, we will look at how we might clean up this file to follow pep8 standards using some of the methods you saw earlier in this course:

* `pylint`
* `autopep8`

As we covered in an earlier lesson, you can run `pylint` with your python script name (e.g. `pylint my_script.py`) to get a score out of 10, while `autopep8 --in-place --aggressive` with your script name will try to force certain aspects of your code to follow PEP8 standards.


# Model Drift

When deploying models into production, it is often the case that the input data changes over time. This shift means that our models may not perform as well over time as they did when the model was originally launched. This process of the model performance degrading over time is known as model drift.

In these cases, you may need to retrain your model and launch a new version of it to replace your existing model. This might mean:

* Finding new features
* Tuning your hyper-parameters
* Finding a new model altogether

## Automated vs. Non-Automated Retraining

There are two methods we might use to retrain and replace the existing model:

* Automated retraining
* Non-automated retraining

If you have a model that needs to be updated really frequently, without needing major feature or model changes, then automated retraining could be a great way to update. The example above where this type of training might be used is with a fraud model.

Alternatively, other models might require new features or new architectures, which are likely best handled by having a human go in and make changes. These changes to a model likely happen less frequently, as considered with a search engine ranking model. In these cases, non-automated retraining is likely the best option. Automating these large changes is likely not worth the additional effort.