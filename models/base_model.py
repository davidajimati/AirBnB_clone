#!/usr/bin/python3

'''
This module contains the Parent class for the AirBnB clone Project
'''

# Import relevant modules
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    ''' BaseModel class Definitions '''

    def __init__(self, *args, **kwargs):
        '''
        Parent class Constructor
        Takes in multiple keyword arguments and creates attributes
        with them.
        '''

        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        self.__dict__[key] = datetime.strptime(
                            value, DATE_FORMAT)

                    elif key[0] == 'id':
                        self.__dict__[key] = str(value)

                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        modifies the behavior of the print statement
        and returns a string representation of the class attributes
        '''
        c_name = self.__class__.__name__
        return "[{}] ({}) {}" .format(c_name, self.id, self.__dict__)

    def save(self):
        '''
        When triggered, updates the updated_at attribute
        '''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Serializing the dictionary of the attributes of instances '''

        dict_objects = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            # For loop to format the updated_at and created_at attributes
            if key == "created_at" or key == "updated_at":
                dict_objects[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict_objects[key] = value
        return dict_objects
