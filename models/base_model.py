#!/usr/bin/python3
"""Module that defines the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel():
    """A class used to define all common attr./methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Initializing the instance attributes."""
        if len(kwargs):
            for key, val in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(val))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the formatted output of the print statement on an instance.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at instance attribute with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of an instance.

        Note:
            __class__ key is created through this function and it value is
            the instance's class.
            created_at and updated_at attributes are converted into isoformat.

        Returns:
            A dictionary containing all the key/values of an instance.
        """
        self.__dict__["__class__"] = str(self.__class__.__name__)
        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)
        self.created_at = self.created_at.isoformat()
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.fromisoformat(self.updated_at)
        self.updated_at = self.updated_at.isoformat()
        return (self.__dict__)
