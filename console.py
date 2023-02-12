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

    def do_User(self, line):
        """Prints all User classes instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["User"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_State(self, line):
        """Prints all State class instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["State"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_Review(self, line):
        """Prints all Review class instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["Review"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_Place(self, line):
        """Prints all Place class instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["Place"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_City(self, line):
        """Prints all City class instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["City"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_BaseModel(self, line):
        """Prints all BaseModel class instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["BaseModel"]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_Amenity(self, line):
        """Prints all Amenity instances"""

        if line == ".all()":
            obj_list = []
            objects = storage.all()
            for obj in objects.values():
                if type(obj) == self.class_map["Amenity"]:
                    obj_list.append(str(obj))
            print(obj_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
