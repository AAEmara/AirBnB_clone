#!/usr/bin/python3
"""user Module that defines a `User` class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel class."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        """Initializing the User class based instance."""
        super().__init__(**kwargs)
