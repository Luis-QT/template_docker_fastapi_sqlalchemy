from typing import Optional
from fastapi import Header
from pydantic import BaseModel

class InputAPI(BaseModel):
    timezone: str
    language: str

def input_api(
    timezone: Optional[str] = Header("America/Lima"),
    language: Optional[str] = Header("EN")
    ):
    return InputAPI(timezone=timezone, language=language)
