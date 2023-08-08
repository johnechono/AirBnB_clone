#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    ''' it defines the Review class '''
    place_id = ''
    user_id = ''
    text = ''
