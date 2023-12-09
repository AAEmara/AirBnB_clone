#!/user/bin/python3
"""amenity Module that defines Amenity Class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inheriting from BaseModel class."""
    name = ""

    def __init__(self, **kwargs):
        """Initializing Amenity Class."""
        super().__init__(**kwargs)
