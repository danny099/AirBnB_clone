#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
"""Base model"""


class BaseModel:
    """Base"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return class name"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update whit the datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        
