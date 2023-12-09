#!/user/bin/python3
"""place Module that defines Place Class."""
from models import BaseModel, City, User, Amenity


class Place(BaseModel):
    """Place class inheriting from BaseModel class."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list()

    def __init__(self, **kwargs):
        """Initializing Place Class."""
        super().__init__(**kwargs)
        city_id = City.id
        user_id = User.id
        amenity_ids = Amenity.id