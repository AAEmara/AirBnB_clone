#!/usr/bin/python3
"""Console module that defines HBNBCommand Class."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HNBCommand Class."""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City",
               "Amenity", "Review"]

    def do_EOF(self, line):
        """Exits the command prompt cleanly when the user passes `EOF`.
        """
        return (True)

    def do_quit(self, line):
        """Exits the command prompt cleanly when the user passes `quit`.
        """
        return (True)

    def emptyline(self):
        return

    def do_create(self, line):
        """Creates a new instance of a given <class name>.
        Note:
            This method saves the new instance to a JSON file,
            and prints the `id`.

        Attr:
            line (string): Contains the user's commands.
        """
        cls_list = HBNBCommand.classes
        if not line:
            print("** class name missing **")
        elif line not in cls_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance.

        Attr:
            line (string): User's commands (class name and id).
        """
        tokens = line.split(" ")
        cls_list = HBNBCommand.classes
        if not line:
            print("** class name missing **")
        elif tokens[0] not in cls_list:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, obj in objs.items():
                if obj.id == tokens[1]:
                    return (print(obj))
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance.

        Attr:
            line (string): User's commands (class name and id).
        """
        tokens = line.split(" ")
        cls_list = HBNBCommand.classes
        if not line:
            print("** class name missing **")
        elif tokens[0] not in cls_list:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, obj in objs.items():
                if obj.id == tokens[1]:
                    del objs[key]
                    storage.save()
                    return ()
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances.

        Attr:
            line (string): User's commands (class name [optional]).
        """
        cls_list = HBNBCommand.classes
        all_list = cls_list.copy()
        all_list.append("")
        if line not in all_list:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            objs_str = list()
            if line != "":
                for key, val in objs.items():
                    if type(val).__name__ == line:
                        objs_str.append(str(val))
            elif line == "":
                for key, val in objs.items():
                    objs_str.append(str(val))
            print(objs_str)

    def do_update(self, line):
        """Updates an instance by saving it to a JSON file.
        Description:
            Usage: update <class name> <id> <attribute name> "<attribute val.>"
                - Only one attribute at a time.
                - Attribute value must be casted to the attribute type.
        Attr:
            line (string): User's commands (class_name id attr_name attr_val).
        """
        tokens = line.split(" ")
        cls_list = HBNBCommand.classes
        if not line:
            return (print("** class name missing **"))
        elif tokens[0] not in cls_list:
            return (print("** class doesn't exist **"))
        elif len(tokens) < 2:
            return (print("** instance id missing **"))
        elif tokens[1]:
            objs = storage.all()
            for key, obj in objs.items():
                if tokens[1] == obj.id:
                    if len(tokens) < 3:
                        return (print("** attribute name missing **"))
                    elif len(tokens) < 4:
                        return (print("** value missing **"))
                    else:
                        obj.__dict__[tokens[2]] = tokens[3].split("\"")[1]
                        obj.save()
                        return ()
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
