#!/user/bin/python3
"""review Module that defines Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting from BaseModel class."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """Initializing Review Class."""
        super().__init__(**kwargs)
