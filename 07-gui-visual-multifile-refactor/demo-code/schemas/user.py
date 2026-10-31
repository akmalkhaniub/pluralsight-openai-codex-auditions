from pydantic import BaseModel, Field

class UserProfileResponse(BaseModel):
    """
    User response schema.
    Starting state: Legacy snake_case fields.
    Target refactor: camelCase JSON aliases for modern frontend client.
    """
    user_id: str
    first_name: str
    last_name: str
    user_role: str
