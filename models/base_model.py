#!/usr/bin/python3
"""Module that defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel():
    """A class used to define all common attr./methods for other classes.
    """
    def __init__(self):
        """Initializing the instance attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns the formatted output of the print statement on an instance.
        """
        return (f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at instance attribute with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of an instance.

        Note:
            __class__ key is created through this function and it value is
            the instance's class.
            created_at and updated_at attributes are converted into isoformat.

        Returns:
            A dictionary containing all the key/values of an instance.
        """
        self.__dict__["__class__"] = str(BaseModel.__name__)
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return (self.__dict__)
