#!/usr/bin/python3
"""This is the console for use with all the CRUD
   Operations for the AirBnB clone project
"""
import cmd
import sys
from models.engine.file_storage import FileStorage


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
        """Creates an instance of BaseModel class.
        """
        from models import classes
        if arg and arg not in classes:
            print("** class doesn't exist **")
        elif not arg:
            print("** class name missing **")
        else:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of instance
           based on the name and id
        """
        from models import classes, storage
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
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
        from models import classes, storage
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
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
        from models import classes, storage
        args = arg.split()
        all_obj = []
        models = storage.all()

        if len(args) == 0:
            for obj in models.values():
                all_obj.append(str(obj))
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in models.items():
                if key.startswith(args[0] + "."):
                    all_obj.append(str(obj))
        print(all_obj)

    def do_update(self, arg):
        """Updates the storage with current data"""
        args = arg.split()
        from models import classes, storage
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        models = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key not in models:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = models[key]
        attr_name = args[2]
        attr_value = "".join(args[3].strip('"'))

        if hasattr(obj, attr_name):
            current_type = type(getattr(obj, attr_name))
            try:
                attr_value = current_type(attr_value)
            except Exception:
                pass
        setattr(obj, attr_name, attr_value)

    def default(self, line):
        if "." in line:
            class_name, method = line.split(".", 1)
            if method == "all()":
                return self.do_all(class_name)

            if method == "count()":
                from models import storage
                models = storage.all()
                sum_class = 0
                for key, value in models.items():
                    identifier = key.split()[0]
                    mode = identifier.split(".")[0]
                    if mode == class_name:
                        sum_class += 1
                print(sum_class)

            if method.startswith("show(") and method.endswith(")"):
                object_id = method[5:-1].strip('"').strip("'")
                return self.do_show(f"{class_name} {object_id}")

            if method.startswith("destroy(") and method.endswith(")"):
                object_id = method[8:-1].strip("'").strip('"')
                return self.do_destroy(f"{class_name} {object_id}")
            


if __name__ == "__main__":
    HBNBCommand().cmdloop()
