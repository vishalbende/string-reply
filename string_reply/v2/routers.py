from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
import re
from string_reply.rules import Rules
import copy

pattern = re.compile(r"^[a-z0-9]*$")



router = APIRouter(prefix="/v2", tags=["String reply service v1"])

@router.get("/reply/{input_tring}")
def rule_based_function(input_tring: str = Path(...)):
    try:
        # input validations 
        input_data = input_tring.split("-")
        if not len(input_data) == 2:
            return JSONResponse(content={
                "message": "Invalid input_string"
            }, status_code=400)
        
        if not pattern.match(input_data[1]):
            return JSONResponse(content={
                "message": "Invalid pattern"
            }, status_code=400)
        
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
    except Exception as e: 
        print(e)
        return JSONResponse(content={"message": "Something went wrong"})
