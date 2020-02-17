#!/usr/bin/python3
"""file storage"""
import json
import os.path
from models.base_model import BaseModel

class FileStorage:
    """"class file storage"""
    __file_path = "././file.json"
    __objects = {}

    def all(self):
        """return objects"""
        return self.__objects

    def new(self, obj):
        """sets the obj whith key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dic = {}
            for key in self.__objects.keys():
                dic[key] = self.__objects[key].to_dict()
            json.dump(dic, f)

    def reload(self):
        """deserialize"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    new = eval(value["__class__"])(**value)
                    self.__objects[key] = new
