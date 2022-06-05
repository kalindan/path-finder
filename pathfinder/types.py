from typing import NamedTuple

class PlaygroundParameters(NamedTuple):
    x_size : int
    y_size : int
    amount_of_obstacles : int

class PossibleMove(NamedTuple):
    move_in_x : int
    move_in_y : int
    distance : int = 0
    is_in_collision : bool = False
    
class PLaygroundMarks(NamedTuple):
    START = "S"
    TARGET = "T"
    OBSTACLE = "#"
    EMPTY_POINT = "."
    PASSED_ROAD = "o"
    