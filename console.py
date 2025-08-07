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
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            models = storage.all()
            if key in models:
                print(models[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance of BaseModel based on its id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            models = storage.all()
            if key in models:
                del models[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        all_obj = []
        models = storage.all()
        
        if len(args) == 0:
            for obj in models.values():
                all_obj.append(str(obj))
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            for key, obj in models.items():
                if key.startswith(args[0] + "."):
                    all_obj.append(str(obj))
        print (all_obj)

    def do_update(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            models = storage.all()
            key = f"{args[0]}.{args[1]}"
            obj = models[key]
            attr_name = args[2]
            attr_value = "".join(args[3].strip('"'))

            if key not in models:
                print("** no instance found**")
                return

            if hasattr(obj, attr_name):
                current_type = type(getattr(obj, attr_name))
                try:
                    attr_value = current_type(attr_value)
                except:
                    pass
            setattr(obj, attr_name, attr_value)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
