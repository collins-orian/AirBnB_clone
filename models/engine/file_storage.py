#!/usr/bin/python3
'''file storage class for the project'''

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as file:
            json.dumps(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
