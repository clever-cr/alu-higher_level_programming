#!/usr/bin/python3
"""define class base"""

import json
import csv


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
