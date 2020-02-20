#!/usr/bin/python3
"""file storage"""
import json
import os.path
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

list_class = {"BaseModel": BaseModel, "State": State, "Amenity": Amenity,
              "Place": Place, "Review": Review, "User": User}
              
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
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json = json.load(f)
            for key in json:
                self.__objects[key] = classes[json[key]["__class__"]](**json[key])
        except:
            pass
