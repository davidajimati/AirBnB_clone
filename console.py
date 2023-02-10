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

            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, line):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
