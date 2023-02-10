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
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class definition for the command line processor
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        print("Exiting.")
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program'''
        print("Exiting.")
        return True

    def emptyline(self):
        print("", end="")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
