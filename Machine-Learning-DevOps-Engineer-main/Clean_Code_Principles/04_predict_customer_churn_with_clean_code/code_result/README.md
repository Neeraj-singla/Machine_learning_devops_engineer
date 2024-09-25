# Churn Prediction Library

This project contains a library for predicting customer churn in a bank. The library includes functions to import data, perform exploratory data analysis (EDA), feature engineering, train models, and store results.

## Project Structure

- `churn_library.py`: Contains the main functions for data import, EDA, feature engineering, and model training.
- `tests/test_churn_library.py`: Contains tests for the functions in `churn_library.py`.
- `data/`: Folder where the CSV data file (`bank_data.csv`) should be located.
- `images/`: Folder where the images generated during EDA and classification reports will be stored.
- `models/`: Folder where the trained models will be saved.
- `logs/`: Folder where the logs generated during script execution will be stored.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/churn-prediction-library.git
    cd churn-prediction-library
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the main script and perform the entire process of data import, EDA, feature engineering, and model training, simply execute:

```bash
python churn_library.py
```

Ensure that the `bank_data.csv` file is located in the `data/` folder before running the script.

## Testing

To run the tests and ensure all functions are working correctly, use `pytest`:

```bash
pytest
```

The tests will verify the following functionalities:

* Data import
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model training

## File Structure
* `churn_library.py`: Main module with functions for data import, EDA, feature engineering, and model training.
* `tests/test_churn_library.py`: Tests to validate the functions in the main module.
* `data/bank_data.csv`: CSV file with input data.
* `images/`: Directory where images generated during EDA and classification reports are saved.
* `models/`: Directory where trained models are saved.
* `logs/churn_library.log`: Log file to track progress and errors during script execution.

## Author
* Jazielinho - [GitHub](https://github.com/Jazielinho) - [LinkedIn](https://www.linkedin.com/in/jahazielponce/)
