from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from fastapi import Request 
from typing import Optional 

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request)->Optional[HTTPAuthorizationCredentials]:
        pass
