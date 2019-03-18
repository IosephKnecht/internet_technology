import random

from ships import OneCellShip, TwoCellShip, ThreeCellShip, FourCellShip, Orientation


class ShipManager:
    __max_range = None
    __matrix = None

    def __init__(self):
        self.__max_range = 10
        self.__matrix = [[0] * self.__max_range for i in range(self.__max_range)]

    __ship_list = [OneCellShip(),
                   OneCellShip(),
                   OneCellShip(),
                   OneCellShip(),
                   TwoCellShip(),
                   TwoCellShip(),
                   TwoCellShip(),
                   ThreeCellShip(),
                   ThreeCellShip(),
                   FourCellShip()]

    def initialize(self):
        ship_count = 0

        while ship_count != self.__max_range:
            ship = self.__ship_list[ship_count]
            position = self.__generate_valid_position()

            ship.set_x(position[0])
            ship.set_y(position[1])

            orientation = self.__define_orientation(ship)

            if orientation is None:
                continue

            self.__insert_cells(ship, orientation)
            ship_count += 1

        # for ship in self.__ship_list:
        #     position = self.__generate_valid_position()
        #
        #     ship.set_x(position[0])
        #     ship.set_y(position[1])
        #
        #     orientation = self.__define_orientation(ship)
        #
        #     if orientation is None:
        #         continue
        #
        #     self.__insert_cells(ship, orientation)

        self.__dehydrate_matrix()
        return self.__matrix

    def __dehydrate_matrix(self):
        for i in list(range(self.__max_range)):
            for j in list(range(self.__max_range)):
                if self.__matrix[i][j] == -1:
                    self.__matrix[i][j] = 0

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

    def __valid_coord(self, coord):
        return 0 <= coord < self.__max_range

    def __valid_coord_tuple(self, coord_tuple):
        for coord in coord_tuple:
            if not self.__valid_coord(coord):
                return False
        return self.__matrix[coord_tuple[0]][coord_tuple[1]] == 0

    def __define_orientation(self, ship):
        lambdas = (lambda check_ship: self.__left_orientation(check_ship),
                   lambda check_ship: self.__right_orientation(check_ship),
                   lambda check_ship: self.__top_orientation(check_ship),
                   lambda check_ship: self.__bottom_orientation(check_ship))

        for func in lambdas:
            orientation = func(ship)

            if orientation is not None:
                return orientation

        return None

    def __generate_valid_position(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
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
