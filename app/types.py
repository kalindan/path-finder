from typing import NamedTuple


class PlaygroundParameters(NamedTuple):
    x_size: int | None
    y_size: int | None
    amount_of_obstacles: int


class PossibleMove(NamedTuple):
    move_in_x: int | None
    move_in_y: int | None
    distance: int = 0
    is_in_collision: bool = False


class PLaygroundMarks:
    START = "S"
    TARGET = "T"
    OBSTACLE = "#"
    EMPTY_POINT = "."
    PASSED_ROAD = "o"
