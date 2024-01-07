from fastapi.security import OAuth2PasswordBearer
from ..models.token_utils import create_token, decode_token
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, APIRouter
from datetime import timedelta
from ..routes.route import users_collection

router = APIRouter()

# password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer for Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Retrieve the current user based on his token.
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if not payload:
        raise credentials_exception
    return payload


# Authenticate the user based on his username and password.
async def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if user and pwd_context.verify(password, user["hashed_password"]):
        token_data = {"sub": user["_id"]}
        access_token_expires = timedelta(minutes=30)
        access_token = create_token(data=token_data, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
