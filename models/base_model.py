#!/usr/bin/python3

'''Module for Base'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel with unique id and current datetime."""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Print BaseModel instance information."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary of instance attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict



