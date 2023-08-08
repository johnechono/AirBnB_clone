#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    ''' it defines the User class '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
