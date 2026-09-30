from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..auth import authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


# loging endpoint:
class LoginRequest(BaseModel):
    username: str
    password: str


# POST /auth/login
@router.post("/login")
def login(data: LoginRequest) -> dict[str, str]:
    if not authenticate_user(data.username, data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    token = create_access_token(data.username)

    return {"access_token": token, "token_type": "bearer"}
