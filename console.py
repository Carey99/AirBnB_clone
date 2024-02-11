#!/usr/bin/python3
"""
Entry point of the project
"""
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    """Class inheriting from cmd"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def do_quit(self, arg):
        """Exits gracefully"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
