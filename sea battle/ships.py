from abc import ABC
from enum import Enum


class Orientation(Enum):
    LEFT = 1,
    RIGHT = 2,
    TOP = 3,
    BOTTOM = 4


class AbstractShip(ABC):
    __x = None
    __y = None
    __length = None
    __identifier = None

    def __init__(self, length, identifier):
        self.__length = length
        self.__identifier = identifier

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def get_length(self):
        return self.__length

    def get_identifier(self):
        return self.__identifier


class OneCellShip(AbstractShip):

    def __init__(self):
        super().__init__(1, 1)


class TwoCellShip(AbstractShip):

    def __init__(self):
        super().__init__(2, 2)


class ThreeCellShip(AbstractShip):

    def __init__(self):
        super().__init__(3, 3)


class FourCellShip(AbstractShip):

    def __init__(self):
        super().__init__(4, 4)
