#!/user/bin/python3
"""city Module that defines City Class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel class."""
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """Initializing City Class."""
        super().__init__(**kwargs)
