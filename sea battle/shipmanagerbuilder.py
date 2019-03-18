from math import sqrt, ceil
import random
import copy

from ships import AbstractShip, Orientation


class ShipManager:
    __ship_list = None
    __matrix = None

    __orientations = list()

    def __init__(self, ship_list, fill_matrix):
        self.__ship_list = copy.deepcopy(ship_list)
        self.__matrix = copy.deepcopy(fill_matrix)

        self.__orientations = (lambda check_ship: self.__left_orientation(check_ship),
                               lambda check_ship: self.__right_orientation(check_ship),
                               lambda check_ship: self.__top_orientation(check_ship),
                               lambda check_ship: self.__bottom_orientation(check_ship))

    def initialize(self):
        ship_count = 0

        while ship_count != self.__matrix.__len__():
            ship = self.__ship_list[ship_count]
            position = self.__generate_valid_position()

            ship.set_x(position[0])
            ship.set_y(position[1])

            orientation = self.__define_orientation(ship)

            if orientation is None:
                continue

            self.__insert_cells(ship, orientation)
            ship_count += 1

        self.__dehydrate_matrix()
        return self.__matrix

    def __insert_cells(self, ship, orientation):
        x = ship.get_x()
        y = ship.get_y()

        execute = None

        if orientation == Orientation.LEFT:
            execute = lambda offset: [x, y - offset]
        elif orientation == Orientation.RIGHT:
            execute = lambda offset: [x, y + offset]
        elif orientation == Orientation.TOP:
            execute = lambda offset: [x - offset, y]
        elif orientation == Orientation.BOTTOM:
            execute = lambda offset: [x + offset, y]

        for i in list(range(ship.get_length())):
            insert_position = execute(i)
            self.__matrix[insert_position[0]][insert_position[1]] = ship.get_identifier()
            self.__hydrate_cell(insert_position)

    def __hydrate_cell(self, position):
        x = position[0]
        y = position[1]

        mark_cells = list()

        mark_cells.append((x - 1, y))
        mark_cells.append((x + 1, y))
        mark_cells.append((x, y + 1))
        mark_cells.append((x, y - 1))
        mark_cells.append((x + 1, y + 1))
        mark_cells.append((x + 1, y - 1))
        mark_cells.append((x - 1, y + 1))
        mark_cells.append((x - 1, y - 1))

        for mark_cell in mark_cells:
            mark_cell_x = mark_cell[0]
            mark_cell_y = mark_cell[1]

            if self.__valid_coord_tuple(mark_cell):
                if self.__matrix[mark_cell_x][mark_cell_y] == 0:
                    self.__matrix[mark_cell_x][mark_cell_y] = -1

    def __dehydrate_matrix(self):
        size = self.__matrix.__len__()
        for i in list(range(size)):
            for j in list(range(size)):
                if self.__matrix[i][j] == -1:
                    self.__matrix[i][j] = 0

    def __define_orientation(self, ship):
        for func in self.__orientations:
            orientation = func(ship)

            if orientation is not None:
                return orientation

        return None

    def __generate_valid_position(self):
        while True:
            # error with size = 0
            size = self.__matrix.__len__() - 1
            x = random.randint(0, size)
            y = random.randint(0, size)
            if self.__matrix[x][y] == 0:
                return (x, y,)

    def __top_orientation(self, ship):
        x = ship.get_x()
        y = ship.get_y()

        for i in list(range(ship.get_length())):
            if not self.__valid_coord_tuple((x - i, y)):
                return None

        return Orientation.TOP

    def __bottom_orientation(self, ship):
        x = ship.get_x()
        y = ship.get_y()

        for i in range(ship.get_length()):
            if not self.__valid_coord_tuple((x + i, y)):
                return None

        return Orientation.BOTTOM

    def __right_orientation(self, ship):
        x = ship.get_x()
        y = ship.get_y()

        for i in range(ship.get_length()):
            if not self.__valid_coord_tuple((x, y + i)):
                return None

        return Orientation.RIGHT

    def __left_orientation(self, ship):
        x = ship.get_x()
        y = ship.get_y()

        for i in range(ship.get_length()):
            if not self.__valid_coord_tuple((x, y - i)):
                return None

        return Orientation.LEFT

    def __valid_coord(self, coord):
        return 0 <= coord < self.__matrix.__len__()

    def __valid_coord_tuple(self, coord_tuple):
        for coord in coord_tuple:
            if not self.__valid_coord(coord):
                return False
        return self.__matrix[coord_tuple[0]][coord_tuple[1]] == 0

    class Builder:
        __ship_list = list()
        __size = None

        def add_ship(self, ship):
            if isinstance(ship, AbstractShip):
                self.__ship_list.append(ship)
            return self

        def assign_size(self, size):
            self.__size = size
            return self

        def build(self):
            fill_matrix = self.__fill_matrix(self.__size)
            return ShipManager(self.__ship_list, fill_matrix)

        def __fill_matrix(self, size):
            fill_lambda = lambda matrix_size: [[0] * matrix_size for i in range(matrix_size)]

            if size is not None:
                condition = self.__check_size(size)
                if condition:
                    return fill_lambda(size)
                else:
                    return fill_lambda(0)
            else:
                calcul_size = ceil(sqrt(self.__calculate_size()))
                return fill_lambda(calcul_size)

        def __check_size(self, size):
            calcul_size = ceil(sqrt(self.__calculate_size()))
            return size >= calcul_size

        def __calculate_size(self):
            if self.__ship_list is None:
                return 0
            else:
                count = 0
                for ship in self.__ship_list:
                    count += (ship.get_length() + 2) * 2 + 2
                return count
