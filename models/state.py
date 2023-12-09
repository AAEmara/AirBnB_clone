#!/user/bin/python3
"""state Module that defines State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class."""
    name = ""

    def __init__(self, **kwargs):
        """Initializing State Class."""
        super().__init__(**kwargs)
