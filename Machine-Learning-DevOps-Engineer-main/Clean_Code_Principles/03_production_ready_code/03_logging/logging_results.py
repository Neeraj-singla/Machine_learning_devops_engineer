
'''
Given two values, return the sum of the two values
'''

from typing import Union
import logging

logging.basicConfig(
    filename='results.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


def sum_vals(first: Union[int, float], second: Union[int, float]) -> Union[int, float, str]:
    '''
    Given two values, return the sum of the two values
    Args:
        first: (int, float)
        second: (int, float)
    Return:
        first + second (int, float, str)
    '''
    try:
        assert isinstance(first, (int, float)), "First value must be an integer or float"
        assert isinstance(second, (int, float)), "Second value must be an integer or float"
        result = first + second
        logging.info("Sum of %s and %s is %s", first, second, result)
        return result
    except AssertionError as assertion_error:
        message = f"Trying to sum the values {first} and {second}: {assertion_error}"
        logging.error(message)
        return message
    except TypeError as type_error:
        message = f"Trying to sum the values {first} and {second}: {type_error}"
        logging.error(message)
        return message
    except (ValueError, OverflowError) as specific_exception:
        message = f"Trying to sum the values {first} and {second}: {specific_exception}"
        logging.error(message)
        return message


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(1, 'way')
    sum_vals('no', 1)
    sum_vals(4, 5)
