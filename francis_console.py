#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBNB clone console. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exits the program"""
        print("Exiting.")
        raise SystemExit

    def do_EOF(self, args):
        """Exits the program"""
        print("Exiting.")
        raise SystemExit

    def do_help(self, args):
        """
        Get help on Commands
        'help' or '?' with no arguments prints a list of commands for which help is available
        'help <command> or '? <command> gives help on <command>
        """

    def emptyline(self):
        "An entered empty line doesn't execute anything"
        pass

    def do_create(self, args):
        """Create new instance of Base Model"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.strip()
        try:
            model = eval(class_name + "()")
            storage.save()
            print(f"{model.id} created")

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Usage: show <class name> <instance id>
        Display the string representation of a class instance of a given id
        """

        arg1 = args.split()
        if len(arg1) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            key = f"{arg1[0]}.{arg1[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Usage: destroy <class name> <instance id>
        deletes an instance of the class name and id then save change into the JSON file
        """

        arg1 = args.split()
        if len(arg1) == 0:
                print("** class name missing **")

        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(arg1) == 1:
            print(" ** instance id missing **")

        else:
            key = arg1[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Usage: all <class name> or all
        Prints all string representation of all instances based or not on <class name>
        """

        arg1 = args.split()
        if len(arg1) == 0:
            objects = storage.all()
            for obj in objects.values():
                    print(obj)
        elif ((len(arg1) > 0) and arg1[0] in HBNBCommand.__classes):
            objects = storage.all(arg1[0])
            for obj in objects.values():
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Update instance based on class name and id by adding or updating attribute (save change into the JSON file)
        """

        arg1 = args.split()
        obj_dict = storage.all()

        if len(arg1) == 0:
            print("** class name missing **")
            return

        class_name = arg1[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg1) == 1:
            print("** instance id missing **")
            return

        else:
            obj = obj_dict.get(class_name + "." + obj_id)
            for key, val in obj_dict.items():
                obj_name = val.__class__.__name__
                obj_id = val.id
                if obj_name == arg1[0] and obj_id == arg1[1].strip('"'):
                    if len(arg1) == 2:
                        print("** attribute name missing **")
                    elif len(arg1) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, arg1[2] and arg1[3])
                        storage.save()
                    return

        print("** no instance found **")


if __name__ - '__main__':
    HBNBCommand().cmdloop()
