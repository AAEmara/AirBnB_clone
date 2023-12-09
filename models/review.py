#!/user/bin/python3
"""review Module that defines Review Class."""
from models import BaseModel, Place, User


class Review(BaseModel):
    """Review class inheriting from BaseModel class."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """Initializing Review Class."""
        super().__init__(**kwargs)
        self.place_id = Place.id
        self.user_id = User.id
