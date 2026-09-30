from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from proyecto_final_integrador.api.auth import authenticate_user, create_access_token
from proyecto_final_integrador.api.schemas import TokenResponse

# router de login:
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> TokenResponse:
    if not authenticate_user(
        form_data.username,
        form_data.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas.",
        )

    return TokenResponse(
        access_token=create_access_token(form_data.username),
    )
