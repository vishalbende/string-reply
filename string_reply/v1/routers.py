

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
import re

pattern = re.compile(r"^[a-z0-9]*$")



router = APIRouter(prefix="/v1", tags=["String reply service v1"])

@router.get("/reply/{input_string}")
def string_reply(input_string: str = Path(..., pattern=r"^[a-z0-9]*$")):
    """ Api to send response in json format
    Args:
        input_string (str, optional): _description_. Defaults to Path(..., pattern=r"^[a-z0-9]*$").

    Returns:
        _type_: JSON response
    """

    try:
        response_data = {
            "data": input_string
        }
        return JSONResponse(content=response_data, status_code=200)
    except Exception as e: 
        print(e)
        return JSONResponse(content={"message": "Something went wrong"}, status_code=500)
