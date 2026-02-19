from pydantic import BaseModel

class UserRegistrationModel(BaseModel):
    """
    User registration model
    """
    email: str
    password: str