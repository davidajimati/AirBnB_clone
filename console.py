#!/usr/bin/python3

"""
 This program contains the entry point of the command interpreter:

    Uses the module cmd
    class definition is: class HBNBCommand(cmd.Cmd):
    implements:
        quit and EOF to exit the program
        help (this action is provided by default by
        cmd but updated and documented)

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
    all_classes = ['BaseModel', 'User', 'State',
                   'Review', 'Place', 'City', 'Amenity']
    class_map = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Place": Place,
        "City": City,
        "Amenity": Amenity
    }

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
        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")

        else:
            state = False
            cls = args[0]
            id = args[1]
            objects = storage.all()
            for k, v in objects.items():
                if k == "{}.{}" .format(cls, id):
                    print(v)
                    state = True

            if state is False:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance"""

        args = args.split()
        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")

        else:
            cls = args[0]
            id = args[1]
            objects = storage.all()
            data = cls + '.' + id
            if data in objects.keys():
                del objects[data]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        Example: $ all BaseModel |or| $ all
        """

        args = args.split()

        if len(args) == 0:
            out = []
            objects = storage.all()
            for item in objects:
                obj_attrs = objects[item]
                out.append(str(obj_attrs))
            print(out)

        else:
            cls = args[0]
            obj_list = []

            if cls in self.all_classes:
                objects = storage.all()
                for obj in objects.values():
                    if type(obj) == self.class_map[cls]:
                        obj_list.append(str(obj))
                print(obj_list)

            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates the attributes of the specified instance"""

        args = args.split()
        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            cls = args[0]
            id = args[1]
            key = args[2]
            try:
                new_val = int(args[3])
            except Exception:
                try:
                    new_val = float(args[3])
                except Exception:
                    new_val = str(args[3].strip('\'"'))

            objects = storage.all()
            key_fmt = "{}.{}" .format(cls, id)
            if key_fmt not in objects.keys():
                print("** no instance found **")
            else:
                focus = objects[key_fmt]
                setattr(focus, key, new_val)

        storage.save()

# Advanced tasks ---------------------------------------------

# Command Parsers ---------------------------------------- Start

    def grand_parser(self, str, cls_name):
        """Delegates the parsing to the right algorithm"""
        if str[-2:] == '")':
            return (self.parse_id(str, cls_name))
        elif str[-6:] == 'show()':
            return (self.show_parser(str, cls_name))
        elif str[-6:] == '.all()':
            return (self.all_parser(str, cls_name))
        elif str[-6:] == 'ount()':
            return self.counter_parser(str, cls_name)

# ------------------------GRAND SEALED------------------------------

    def show_parser(self, string, cls_name):
        '''Parses command and returns list'''
        res = (string.split('.'))
        return (self.iid_printer(cls_name, res[1], res[2]))

# ------------------------SHOW SEALED ------------------------------

    def all_parser(self, string, cls_name):
        '''Parses command and returns list'''
        res = string.split('.')
        return (self.printer_engine(cls_name, res[1]))

# ------------------------ALL SEALED ------------------------------

    def counter_parser(self, string, cls_name):
        '''Parses command and returns list'''
        res = string.split('.')
        return (self.counter_engine(cls_name, res[1]))

# ------------------------COUNTER_PARSER SEALED ---------------------

    def parse_id(self, string, cls_name):
        '''Parses command and returns list'''
        real = []

        pre = string.split('.')
        real.append(pre[0])

        pre2 = pre[1].split('("')
        real.append(pre2[0])

        pre3 = pre2[1].split('")')
        real.append(pre3[0])
        return (self.iid_printer(cls_name, real[1], real[2]))

# -------------------- PARSE_ID SEALED ------------------------------

# -------------------- Engine area ----------------------------------

# All printer Engine
    def printer_engine(self, cls_name, command):
        '''Returns list of all instances of a class'''

        if command == "all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map[cls_name]:
                    obj_list.append(str(obj))
            return (obj_list)

# --------------Printer Engine sealed ---------------------------------

    def do_User(self, args):
        """Prints all User classes instances"""
        print(self.grand_parser(args, "User"))

    def do_State(self, args):
        """Prints all State class instances"""
        print(self.grand_parser(args, "State"))

    def do_Review(self, args):
        """Prints all Review class instances"""
        print(self.grand_parser(args, "Review"))

    def do_Place(self, args):
        """Prints all Place class instances"""
        print(self.grand_parser(args, "Place"))

    def do_City(self, args):
        """Prints all City class instances"""
        print(self.grand_parser(args, "City"))

    def do_BaseModel(self, args):
        """Prints all BaseModel class instances"""
        print(self.grand_parser(args, "BaseModel"))

    def do_Amenity(self, args):
        """Prints all Amenity instances"""
        print(self.grand_parser(args, "Amenity"))

# separator --------------------------------------------
# Counter Engine Function

    def counter_engine(self, cls_name, command):
        """Counts the number of instances in a Class"""
        if command == "count()":
            count = 0
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map[cls_name]:
                    count += 1
            return (count)

# Engine sealed ----------------------------------------

# -------------------- COUNT CITY ----------------------
    def do_User(self, args):
        """Prints User instances count """
        print(self.grand_parser(args, "User"))

    def do_State(self, args):
        """Prints State instances count """
        print(self.grand_parser(args, "State"))

    def do_Review(self, args):
        """Prints Review instances count """
        print(self.grand_parser(args, "Review"))

    def do_Place(self, args):
        """Prints Place instances count """
        print(self.grand_parser(args, "Place"))

    def do_City(self, args):
        """Prints City instances count """
        print(self.grand_parser(args, "City"))

    def do_BaseModel(self, args):
        """Prints BaseModel instances count """
        print(self.grand_parser(args, "BaseModel"))

    def do_Amenity(self, args):
        """Prints Amenity instances count """
        print(self.grand_parser(args, "Amenity"))

# Separator ------------------------------------

# Instance attributes **SHOW** ENGINE
    def iid_printer(self, cls_name, command, iid):

        if command == "show":
            key = "{}.{}".format(cls_name, iid)
            objects = storage.all()
            for obj, val in objects.items():
                if obj == key:
                    return (val)
            return("** no instance found **")

# Separator --------------------------------------------

    def do_User(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "User"))

    def do_State(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, 'State'))

    def do_Review(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "Review"))

    def do_Place(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "Place"))

    def do_City(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "City"))

    def do_BaseModel(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "BaseModel"))

    def do_Amenity(self, args):
        """
        retrieve an instance based on its ID: <class name>.show(<id>)
        """
        print(self.grand_parser(args, "Amenity"))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
