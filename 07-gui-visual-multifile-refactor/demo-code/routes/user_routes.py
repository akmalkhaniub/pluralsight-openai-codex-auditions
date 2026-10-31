from fastapi import APIRouter
from schemas.user import UserProfileResponse
from services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.get("/{user_id}", response_model=UserProfileResponse)
def fetch_user(user_id: str):
    """
    Retrieves user profile and serializes via UserProfileResponse schema.
    """
    service = UserService()
    profile = service.get_user_profile(user_id)
    return profile
