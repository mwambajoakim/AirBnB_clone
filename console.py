#!/usr/bin/python3
"""This is the console for use with all the CRUD
   Operations for the AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = storage.reload()

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
            arg.save()
            print(arg.id)

    def do_show(self, arg):
        """Prints string representation of instance
           based on the name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** class id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            models = storage.all()
            if key in models:
                print(models[key])
            else:
                print("** instance doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
