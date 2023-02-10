#!/usr/bin/python3

"""
 This program contains the entry point of the command interpreter:

    Uses the module cmd
    class definition is: class HBNBCommand(cmd.Cmd):
    implements:
        quit and EOF to exit the program
        help (this action is provided by default by cmd but updated and documented)

    a custom prompt: (hbnb)
    an empty line + ENTER doesn't execute anything
    Not be executed when imported
"""
import traceback
import cmd
from sys import argv
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class definition for the command line processor
    """
    prompt = '(hbnb) '
    all_classes = ['BaseModel', 'User', 'State', 'Review', 'Place', 'City', 'Amenity']

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        """An entered empty line doesn't execute anything"""
        print("", end="")

    def do_create(self, args):
        '''Creates a new class instance, taking commands from the CLI'''
        args = args.split()
        if len(args) != 1:
            print("** class name missing **")
        else:
            try:
                latest = eval("{}()".format(args[0]))
                storage.save()
                print(latest.id)

            except Exception:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Returns the string representation an instance """

        args = args.split()

        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")

        else:
            data = storage.all().get("{}.{}" .format(args[0], args[1]))
            if data is None:
                print("** no instance found **")
            else:
                print(data)

    def do_destroy(self, args):
        """Deletes an instance"""

        args = args.split()
        target = args[0]
        iid = args[1]
        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")

        else:
            data = storage.all().get(target + '.' + iid)
            if data is None:
                print("** no instance found **")
            else:
                del data
                storage.save()

    def do_all(self, args):
        args = args.split()
        target = args[0]
        if len(args) == 0:
            objects = storage.all()
            for item in objects:
                print(item)
        else:
            out = []
            idx = 0
            if target in self.all_classes:
                objects = storage.all().get(target)
                for item in objects:
                    out[idx] = item
                    idx += 1
                print(out)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        cls_n = args[0]
        iid = args[1]
        attr_n = args[2]
        new_val = args[3]

        if len(args) < 1:
            print("** class name missing **")

        elif iid < 2:
            print("** instance id missing **")

        elif cls_n not in self.all_classes:
            print("** class doesn't exist **")

        elif attr_n not in self.all_classes:
            print("** attribute name missing **")

        elif new_val not in self.all_classes:
            print("** value missing **")

        else:
            data = storage.all().get(cls_n + '.' + iid)
            if data is None:
                print("** no instance found **")
            else:
                object = storage.all([cls_n])
                for k, v in object.items():
                    if k == attr_n:
                        object[attr_n] = new_val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
