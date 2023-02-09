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

        try:
            with open(self.__file_path, 'x') as file:
                json.dump({k: v.to_dict()
                           for k, v in self.__objects.items()}, file)

        except FileExistsError:
            with open(self.__file_path, 'r') as file:
                existing_cont = json.load(file)

                data = {k: v.to_dict()
                        for k, v in self.__objects.items()}

            with open(self.__file_path, 'w') as fi:
                fi.write('\n')
                fi.write(json.dump(data, fi))

    def reload(self):
        ''' reloads objects from a JSON file '''

        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    self.__objects[k] = v
