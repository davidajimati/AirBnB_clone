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
        self.__objects["{}.id".format(obj.__class__.__name__)] = obj

    def save(self):
        '''
        saves __objects to the JSON file "file.json"
        and keeps a separate record of every instance
        '''

        with open(self.__file_path, 'w') as file:
            cls_n = self.__class__.__name__
            idn = self.__objects["id"]
            format = ("{}.{}".format(cls_n, idn))
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[format] = v.to_dict()
            json.dump(json_dict, file)

    def reload(self):
        ''' reloads objects from a JSON file '''
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    self.__objects[k] = v
