
import copy
from string_reply.rules import Rules


def calculte_input(input_data):
    """
     - function to validate and run all required rules
     - this logic is not limited to two digit rule only. Can process any number of rules.
    """
    
    # initialize rule class 
    rule_obj = Rules()

    # collect functions 
    all_functions = []
    str_input = input_data[1]
    rules_data = input_data[0]
    
    for data in rules_data:
        rule_ = f"rule_{data}"
        rule_funct = getattr(rule_obj, rule_, None)

        if not rule_funct:
            return 400, {
                "message": "Invalid input"
            }

        all_functions.append(rule_funct)
        
    # run collected functions
    for function in all_functions:
        str_input = function(str_input)
        
    return 200, {
        "data": str_input
    }
    