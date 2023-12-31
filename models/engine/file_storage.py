#!/usr/bin/python3
"""Module that defines the FileStorage Class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage Class that serializes instances and deserializes JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Creates a dict. with `<class name>.id` (key) and its (value)
        are the objects given.

        Attr:
            obj (dictionary): Objects to be set as a value to the
                              `<class name>.id` key.
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the Objects to a JSON file."""
        filename = FileStorage.__file_path
        with open(filename, mode='w', encoding="utf-8") as w_file:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                w_file)

    def reload(self):
        """Deserializes the JSON file to Objects."""
        try:
            filename = FileStorage.__file_path
            with open(filename, mode='r', encoding="utf-8") as r_file:
                py_obj = json.load(r_file)
        except FileNotFoundError:
            pass
        else:
            for key, val in py_obj.items():
                cls_name = val["__class__"]
                FileStorage.__objects[key] = eval(cls_name)(**val)
