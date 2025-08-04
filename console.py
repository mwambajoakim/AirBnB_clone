#!/usr/bin/python3
"""This is the console for use with all the CRUD
   Operations for the AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """Creates an instance of BaseModel.
        """
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
        elif not arg:
            print("** class name missing **")
        else:
            arg = BaseModel()
            print(arg.id)
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
