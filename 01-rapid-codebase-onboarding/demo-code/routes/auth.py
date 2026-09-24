from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from middleware.rate_limiter import apply_rate_limit
from middleware.token_validator import verify_client_identity
from services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["Authentication"])

class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    payload: RegisterRequest,
    _rate_limit: None = Depends(apply_rate_limit),
    client_info: dict = Depends(verify_client_identity)
):
    """
    User registration entry point.
    Flows through rate limiting, client identity verification,
    and delegates to UserService for hashing and persistence.
    """
    service = UserService()
    result = await service.create_user(
        email=payload.email,
        username=payload.username,
        password=payload.password,
        origin_ip=client_info.get("ip")
    )
    return {"status": "success", "user": result}
