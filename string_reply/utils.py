
import copy
from fastapi.responses import JSONResponse
from string_reply.rules import Rules


def calculte_input(input_data):
    """
     - function to validate and run all required rules
     - this logic is not limited to two digit rule only. Can process any number of rules.
    """
    
    # convert rules to array         
    rules_data = list(input_data[0])
    
    # initialise rule class 
    rule_obj = Rules()

    # check inputs and collect functions 
    all_functions = []
    str_input = input_data[1]
    for data in rules_data:
        rule_ = f"rule_{data}"
        rule_funct = getattr(rule_obj, rule_, None)

        if not rule_funct:
            return JSONResponse(content={"message": "Invalid input"}, status_code=400)
        
        all_functions.append(rule_funct)
    
    # run collected functions
    for function in all_functions:
        return_string = function(str_input)
        str_input = copy.deepcopy(return_string)
        
    return JSONResponse(   
        content={
            "data": str_input
        }, 
        status_code=200
    )
    