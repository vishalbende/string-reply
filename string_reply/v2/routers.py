from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from string_reply.utils import calculte_input
import re


pattern = re.compile(r"^[a-z0-9]*$")

router = APIRouter(prefix="/v2", tags=["String reply service v1"])

@router.get("/reply/{input_string}")
def rule_based_function(input_string: str = Path(...)):
    try:
        # input validations 
        input_data = input_string.split("-")
        if not len(input_data) == 2:
            return JSONResponse(content={
                "message": "Invalid input_string"
            }, status_code=400)
        
        if not pattern.match(input_data[1]):
            return JSONResponse(content={
                "message": "Invalid pattern"
            }, status_code=400)
        
        status_code, content = calculte_input(input_data)  
        
        return JSONResponse(content=content, status_code=status_code)
    except Exception as e: 
        print(e)
        return JSONResponse(content={"message": "Something went wrong"})
