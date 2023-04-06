#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base model class that defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance with a unique id, created_at and updated_at datetime.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]
            self.updated_at = kwargs["updated_at"]

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
