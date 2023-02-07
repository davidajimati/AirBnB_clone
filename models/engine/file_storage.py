#!/usr/bin/python3
'''
Storage engine: Manages Serialization and Deserialization
Saves Python Dict to JSON and converts it back
'''
import json
from os import path


class FileStorage:
    __file_path = "database.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(self.__class__.__name__, self.id)] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        if path.exists(self.__file_path):
            self.__objects = json.load(self.__file_path)
