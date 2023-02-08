#!/usr/bin/python3

'''
This module contains the Parent class for the AirBnB clone Project
'''

# Import relevant modules
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    ''' BaseModel class Definitions '''

    def __init__(self, *args, **kwargs):
        '''
        Parent class Constructor
        Takes in multiple keyword arguments and creates attributes
        with them.
        '''
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        # check if storage instance is not present in kwargs, create it
        if "storage" not in kwargs:
            storage.new(self)

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key], DATE_FORMAT)
                    elif key == 'id':
                        self.__dict__[key] = str(value)
                    else:
                        self.key = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' modifies the behavior of the print statement'''
        c_name = self.__class__.__name__
        return "[{}] ({}) {}" .format(c_name, self.id, self.__dict__)

    def save(self):
        ''' When triggered, updates the updated_at attribute '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Serializing the dictionary of the attributes of instances '''
        map_objects = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            # For loop to format the updated_at and created_at attributes
            if key == "created_at" or key == "updated_at":
                map_objects[key] = self.__dict__[
                    key].strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                map_objects[key] = self.__dict__[key]
        return map_objects
