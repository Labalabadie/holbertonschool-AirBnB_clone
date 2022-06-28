#!/usr/bin/python3
""" Class definition """
import json
from models.user import User


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                self.__objects = json.load(f)
        except Exception:
            pass