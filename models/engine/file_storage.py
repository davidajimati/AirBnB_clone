#!/usr/bin/python3
'''
Storage engine: Manages Serialization and Deserialization
Saves Python Dict to JSON and converts it back
'''
import json
from os import path


class FileStorage:
    ''' Class declaration '''

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        ''' returns the objects dictionary '''
        return self.__objects

    def new(self, obj):
        ''' creates a new instance '''
        self.__objects["{}.{}".format(self.__class__.__name__, self.id)] = obj

    def save(self):
        ''' saves an objects into a JSON file '''
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        ''' reloads objects from a JSON file '''
        if path.exists(self.__file_path):
            self.__objects = json.load(self.__file_path)
