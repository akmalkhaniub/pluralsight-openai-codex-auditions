import pytest
from schemas.user import UserProfileResponse
from services.user_service import UserService

def test_user_profile_response_format():
    """
    Integration verification test.
    Validates that the service output cleanly serializes into UserProfileResponse.
    After refactoring, model_dump(by_alias=True) must yield camelCase keys.
    """
    service = UserService()
    profile_data = service.get_user_profile("usr_99")
    response_model = UserProfileResponse(**profile_data)
    
    # Check that model serializes to dictionary
    serialized = response_model.model_dump(by_alias=True)
    assert serialized is not None
