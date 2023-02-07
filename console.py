#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

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
        """Get help on Commands
        'help' or '?' with no arguments prints a list of commands for which help is avaiable
        'help <command> or '? <command> gives help on <command>'"""

    def emptyline(self):
        "An entered empty line doesn't execute anything"
        pass

    def do_create(self, args):
        """Create new instance of Base Model"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.strip():
        try:
            model = eval(class_name + "()")
            storage.save()
            print(f"{model.id} created")

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Usage: show <class name> <instance id>
        Display the string representation of a class instance of a given id"""
        
        arg1 = arg.split()
        if len(arg1) == 0:
            print("** class name missing **")

        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **)

        elif 

        try:


if __name__ - '__main__':
    HBNBCommand().cmdloop()
