#!/usr/bin/python3

import cmd

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

if __name__ - '__main__':
    HBNBCommand().cmdloop()
