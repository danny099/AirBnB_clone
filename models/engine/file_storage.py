#!/usr/bin/python3
"""file storage"""
import json
import os.path


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
            f.write(json.dumps(self.__objects))
    
    def reload(self):
        """deserialice"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.load(f)
        