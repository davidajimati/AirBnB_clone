#!/usr/bin/python3
'''
Storage engine: Manages Serialization and Deserialization
Saves Python Dict to JSON and converts it back
'''
import json
from os import path


class FileStorage:
    ''' Class declaration '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the objects dictionary '''
        return self.__objects

    def new(self, obj):
        ''' creates a new instance '''
        self.__objects["{}.id".format(obj.__class__.__name__)] = obj
        obj.to_dict()

    def save(self):
        ''' saves an objects into a JSON file '''
        with open(self.__file_path, 'w+') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        ''' reloads objects from a JSON file '''

        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass