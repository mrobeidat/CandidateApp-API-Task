# token_utils.py
from datetime import datetime, timedelta
from typing import Any, Dict
from jose import JWTError, jwt
import secrets

# Defining Encoding and Decoding algo for JWTs
ALGORITHM = "HS256"


def generate_secret_key() -> str:
    return secrets.token_urlsafe(32)


SECRET_KEY = generate_secret_key()


# Creating a JWT token
def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Decode the JWT token
def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return {}
