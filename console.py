#!/usr/bin/python3
"""Console module that defines HBNBCommand Class."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HNBCommand Class."""
    prompt = "(hbnb) "

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
        """Creates a new instance of `BaseModel`
        Note:
            This method saves the new instance to a JSON file,
            and prints the `id`.

        Attr:
            line (string): Contains the user's commands.
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance.

        Attr:
            line (string): User's commands (class name and id).
        """
        tokens = line.split(" ")
        if not line:
            print("** class name missing **")
        elif tokens[0] != "BaseModel":
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
        if not line:
            print("** class name missing **")
        elif tokens[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, obj in objs.items():
                if obj.id == tokens[1]:
                    del objs[key]
                    return ()
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances.

        Attr:
            line (string): User's commands (class name [optional]).
        """
        if line not in ["BaseModel", ""]:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            objs_str = list()
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
        if tokens[0] != "BaseModel":
            return (print("** class name missing **"))
        elif tokens[0] not in ["BaseModel"]:
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
                        return ()
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
