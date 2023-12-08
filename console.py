#!/usr/bin/python3
"""Console module that defines HBNBCommand Class."""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
