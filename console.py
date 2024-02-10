#!/usr/bin/python3
"""Cmd interpreter"""
import cmd
import sys


class Myconsole(cmd.Cmd):
    """Class inheriting from cmd"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the console"""
        print()
        return True

    def do_quit(self, arg):
        """Exits gracefully"""
        return True


if __name__ == "__main__":
    my_console = Myconsole(stdin=sys.stdin, stdout=sys.stdout)

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            line = file.readlines()
        my_console.onecmd('\n'.join(lines))
    else:
        my_console.cmdloop()
