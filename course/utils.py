"""
Below are various simple utility methods we use in many of the notebooks.
To use just:

import utils

utils.float_to_dollars(32.00)

"""

def float_to_dollars(value:float) -> str:
    """
    Take in a float (32.00) 
    """
    return  f"${value:,.2f}" 


def dollar_str_to_float(value:str) -> float:
    return float(value.replace("$", "").replace(",", "_"))


def group_salary(value:float) -> str:
    if value > .95:
        return 'top'
    elif value < .95 and value > .50:
        return 'mid'
    return 'low'