import datetime
import os
from hashlib import sha256

from dotenv import load_dotenv
from jose import jwt, JWTError
from passlib.context import CryptContext

from ..Settings import Settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_access_token(data: dict) -> str:
    """
    Create user's access JWT token

    :param data: user login data
    :return: JWT token
    """
    load_dotenv()

    to_encode = data.copy()
    token_expires_in = int(os.getenv(Settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=token_expires_in)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, os.getenv(Settings.API_SECRET_KEY), algorithm=os.getenv(Settings.ALGORITHM))


def verify_access_token(token: str) -> dict | None:
    """
    Verify access JWT token

    :param token: access JWT token
    :return: toke payload
    """
    try:
        payload = jwt.decode(token, os.getenv(Settings.API_SECRET_KEY), algorithms=[os.getenv(Settings.ALGORITHM)])
        return payload
    except JWTError:
        return None
