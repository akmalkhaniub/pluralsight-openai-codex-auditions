class UserService:
    """
    Business service returning user details.
    Starting state: Returns dictionary with snake_case keys.
    """
    def get_user_profile(self, user_id: str) -> dict:
        # Mock database lookup
        return {
            "user_id": user_id,
            "first_name": "Jordan",
            "last_name": "Miller",
            "user_role": "Platform Engineer"
        }
