#!/usr/bin/python3
''' it creates the base model '''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''
            it creates  new base model instance
            or recreates base model instance from the dictionary
        '''
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        ''' it defines custom string representation of an object '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' it updates the updated_at attribute when called '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            it creates a custom dictionary from __dict__
            (i.e dictionary of instance attributes)
        '''
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        # the __class__ key is needed to recreate the object
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
