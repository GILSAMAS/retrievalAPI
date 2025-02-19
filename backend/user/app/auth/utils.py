from fastapi import Depends
from sqlmodel import Session
from app.settings import JWT_SECRET
from app.settings import JWT_ALGORITHM
from app.settings import ACCESS_TOKEN_EXPIRY
from app.db import get_session
from passlib.context import CryptContext
from datetime import timedelta
from datetime import datetime
from typing import Dict
import jwt
import uuid

blacklist = set()


passwd_context = CryptContext(schemes=["bcrypt"])


def generate_passwd_hash(password: str) -> str:
    return passwd_context.hash(password)


def verify_passwd(password: str, hashed_password: str) -> bool:
    return passwd_context.verify(password, hashed_password)


def create_access_token(
    user_data: Dict, expiry: timedelta = None, refresh: bool = False
) -> str:
    payload = {}
    payload["user"] = user_data
    payload["exp"] = datetime.now() + (
        expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh
    token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decode_token(token: str) -> Dict:
    try:
        token_data = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return token_data
    except jwt.PyJWKError as e:
        print(e)


def token_in_blacklist(jti: str) -> bool:
    if jti in blacklist:
        return True
    return False


def add_jti_to_blocklist(jti: str) -> None:
    blacklist.add(jti)


# admin
[
    "adding users",
    "change roles",
    "crud on users",
    "book submissions",
    "crud on reviews",
    "crud on reviews",
    "revoking access",
]

# user
[
    "crud on their own book submissions",
    "crud on their own reviews",
    "crud on their own accounts",
]
