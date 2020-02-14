#!/usr/bin/python3
"""file storage"""


class FileStorage:
    """"class file storage"""
    def __init__(self):
        """init function"""
        __file_path = "./file.json"
        __objects = {}

    def all(self):
        """return objects"""
        return self.__objects
    
    def new(self, obj):
        """sets the obj whith key"""
        

        
