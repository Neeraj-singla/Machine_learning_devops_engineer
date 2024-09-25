def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    # try to return the fraction but if the denominator is zero
    # catch the error and return a string saying:
    # "denominator cannot be zero"
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "denominator cannot be zero"
    except TypeError:
        if not isinstance(numerator, (int, float)):
            return f"numerator must be of type float. Got {type(numerator)} instead."
        if not isinstance(denominator, (int, float)):
            return f"denominator must be of type float. Got {type(denominator)} instead."
        return f"numerator and denominator must be of type float. Got {type(numerator)} and {type(denominator)} instead."
    except OverflowError:
        return f"numerator and denominator must be smaller values. Got {numerator} and {denominator} instead."
    except Exception as e:
        return f'''An error occurred while trying to divide the values {numerator} and {denominator}: {e}'''


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    # try to split based on spaces and return num of words
    # but if text isnt a string return "text argument must be a string"
    try:
        return len(text.split())
    except TypeError as e:
        return f"An error occurred while trying to split the text: {text}. Error: {e}"
    except AttributeError as e:
        return f"text argument must be a string. Text: {text}. Error: {e}"
    except Exception as e:
        return f"An error occurred while trying to split the text: {text}. Error: {e}"


if __name__ == '__main__':
    print(divide_vals(4, 2))
    print(divide_vals(4, 0))
    print(divide_vals(4, '2'))
    print(divide_vals('4', '2'))
    print(divide_vals(4, 2**1000))
    print(num_words('hello world'))
    print(num_words(4))
    print(num_words(4.0))
    print(num_words(('hello world', 'hello world')))

