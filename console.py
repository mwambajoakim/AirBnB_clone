#!/usr/bin/python3
"""This is the console for use with all the CRUD
   Operations for the AirBnB clone project
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """Checks end of file. If true, exits gracefully.
        """
        return True

    def do_quit(self, line):
        """Exit the command line once the quit is called
        """
        print("See you next time!")
        return True

    def emptyline(self):
        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
