#!/usr/bin/python3
'''
Storage engine: Manages Serialization and Deserialization
Saves Python Dict to JSON and converts it back
'''
import json
from os import path


class FileStorage:
    '''
    Class for file storage
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the objects dictionary '''
        return self.__objects

    def new(self, obj):
        ''' creates a new instance '''
        name_fmt = "{}.{}".format(
            obj.__class__.__name__, str(obj.id))

        self.__objects[name_fmt] = obj

    def save(self):
        '''
        saves __objects to the JSON file "file.json"
        and keeps a separate record of every instance
        '''

        objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objects, f)

    def reload(self):
        ''' reloads objects from a JSON file '''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classmap = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}

        try:
            with open(self.__file_path) as f:
                objects = json.load(f)

            for obj_dict in objects.values():
                class_string = obj_dict["__class__"]
                cls_name = classmap[class_string]
                if cls_name:
                    obj = cls_name(**obj_dict)
                    self.new(obj)

        except (FileNotFoundError):
            pass
