from enum import Enum


class Type(Enum):
    FACTORY = 1
    CITY = 2


class Point:

    def __init__(self, type, index, value):
        self.__type = type
        self.__index = index
        self.__value = value

    @property
    def get_type(self):
        return self.__type

    @property
    def get_index(self):
        return self.__index

    @property
    def get_value(self):
        return self.__value