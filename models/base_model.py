#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
"""Base model"""

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Base"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                dic = {}
                dic[key] = value
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.strptime(value, time)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, time)
        else:
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
        info = self.__dict__.copy()
        info['__class__'] = self.__class__.__name__
        info['created_at'] = self.created_at.isoformat()
        info['updated_at'] = self.updated_at.isoformat()
        return info

