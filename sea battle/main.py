from shipmanagerbuilder import ShipManager
from ships import OneCellShip, TwoCellShip, ThreeCellShip, FourCellShip
import datetime


def calculate_diff(time_delta):
    minutes = int(time_delta.seconds / 60)
    seconds = int(time_delta.seconds % 60)
    return '{0}:{1}'.format(minutes, seconds)


start_time = datetime.datetime.now()

shipmanager_builder = ShipManager.Builder() \
    .add_ship(OneCellShip()) \
    .add_ship(OneCellShip()) \
    .add_ship(OneCellShip()) \
    .add_ship(OneCellShip()) \
    .add_ship(TwoCellShip()) \
    .add_ship(TwoCellShip()) \
    .add_ship(TwoCellShip()) \
    .add_ship(ThreeCellShip()) \
    .add_ship(ThreeCellShip()) \
    .add_ship(FourCellShip()) \
    .build()

fill_matrix = shipmanager_builder.initialize()

end_time = datetime.datetime.now()

for row in fill_matrix:
    print(row)

print()

print('Time passed - {0}'.format(calculate_diff(end_time - start_time)))
