from enum import Enum, auto
from functools import reduce
from typing import NamedTuple
from click import clear
import random as rd
import numpy as np
import time
from pymonad.tools import curry
from pymonad.reader import Pipe

START = "S"
TARGET = "T"
OBSTACLE = "#"
EMPTY_POINT = "."
PASSED_ROAD = "o"

DIRECTIONS = ((-1,0),
              (1,0),
              (0,-1),
              (0,1))

DELAY = 0.01

RIDICULOUSLY_BIG_DISTANCE = 10000

class PlaygroundParameters(NamedTuple):
    x_size : int
    y_size : int
    amount_of_obstacles : int
    
class PossibleMove(NamedTuple):
    move_in_x : int
    move_in_y : int
    distance : int = 0
    is_in_collision : bool = False
    
class SearchState(Enum):
    MOVE_AVAILABLE = auto()
    NO_MOVES_AVAILABLE = auto()
    TARGET_REACHED = auto()
    

@curry(2)
def generate_empty_playground(x_size, y_size) -> list[list[str]]:
    
    return [[OBSTACLE if i == 0 or i == x_size-1 or j == 0 or j == y_size-1 else EMPTY_POINT for i in range(x_size)] for j in range(y_size)]

@curry(2)
def add_obstacles_to_playground(number_of_obstacles, playground) -> list[list[str]]:
    
    new_playground = playground
    for _ in range(number_of_obstacles):
        new_playground[rd.randint(1,len(new_playground)-2)][rd.randint(1,len(new_playground[0])-2)] = OBSTACLE

    return new_playground

@curry(2)
def add_point_to_playground(point, playground) -> list[list[str]]:
    
    new_playground = playground
    new_playground[rd.randint(1,len(new_playground)-2)][rd.randint(1,len(new_playground[0])-2)] = str(point)
    
    return new_playground

def generate_playground_with_obstacles(playground_parameters : PlaygroundParameters) -> list[list[str]]:
    
    return (Pipe(generate_empty_playground(playground_parameters.x_size, playground_parameters.y_size))
            .then(add_obstacles_to_playground(playground_parameters.amount_of_obstacles))
            .then(add_point_to_playground(START))
            .then(add_point_to_playground(TARGET))
            .flush())
    
@curry(2)
def is_move_in_collision(playground, move : PossibleMove,) -> PossibleMove:
    
    if playground[move.move_in_x][move.move_in_y] == OBSTACLE or playground[move.move_in_x][move.move_in_y] == PASSED_ROAD:
        
        return PossibleMove(move.move_in_x, move.move_in_y, 0, is_in_collision=True)
    
    return move

@curry(2)
def get_distance_from_target(target_point, move : PossibleMove) -> PossibleMove:

    distance = np.abs(move.move_in_x - target_point[0]) + np.abs(move.move_in_y - target_point[1])
        
    return PossibleMove(move.move_in_x, move.move_in_y, distance, move.is_in_collision)

def check_move_for_collision_and_distance(move : PossibleMove, target_point, playground) -> PossibleMove:
    
    return (Pipe(is_move_in_collision(playground, move))
             .then(get_distance_from_target(target_point))
             .flush())

def generate_possible_moves(actual_point) -> tuple[PossibleMove]:
    
    return tuple(PossibleMove(move_in_x = actual_point[0] + direction[0], move_in_y = actual_point[1] + direction[1]) for direction in DIRECTIONS)

@curry(3)
def check_all_moves_for_collision_and_distance(target_point, playground, possible_moves : tuple[PossibleMove]) -> tuple[PossibleMove]:

    return [check_move_for_collision_and_distance(move, target_point, playground) for move in possible_moves]

def filter_feasible_moves(checked_moves : tuple[PossibleMove]) -> tuple[PossibleMove]:
    
    return tuple(filter(lambda x: x.is_in_collision == False, checked_moves))

def select_next_move(filtered_moves : tuple[PossibleMove]) -> PossibleMove:

    if filtered_moves == (): return None
    
    else:
        next_move : PossibleMove = reduce(lambda x, y: x if x.distance < y.distance else y, 
                                          filtered_moves, PossibleMove(None, None, distance = RIDICULOUSLY_BIG_DISTANCE))
        return next_move


def print_current_move(actual_point, playground) -> list[list[str]]:
    
    new_playground = playground
    if new_playground[actual_point[0]][actual_point[1]] != TARGET and new_playground[actual_point[0]][actual_point[1]] != START:
        new_playground[actual_point[0]][actual_point[1]] = PASSED_ROAD
        
    return new_playground

def print_playground(playground) -> None:
    
    clear()
    [print(reduce(lambda x, y: x + y, row)) for row in playground]
    time.sleep(DELAY)

def print_playground_with_current_move(actual_point, playground) -> None:
    
    return (Pipe(print_current_move(actual_point, playground))
              .then(print_playground)
              .flush()) 

def is_in_target(next_move: PossibleMove) -> bool:
    
    return next_move.distance == 0

def is_next_move_unavailable(next_move: PossibleMove) -> bool:
    
    return next_move == None

@curry(4)
def evaluate_next_progress(actual_point, target_point, playground, next_move: PossibleMove) -> SearchState:
    
    if is_next_move_unavailable(next_move): return SearchState.NO_MOVES_AVAILABLE
        
    print_playground_with_current_move(actual_point, playground)
      
    if is_in_target(next_move): return SearchState.TARGET_REACHED 
        
    return find_path((next_move.move_in_x, next_move.move_in_y), target_point, playground)
    
def is_target_reached(search_state: SearchState):
    
    if search_state == SearchState.NO_MOVES_AVAILABLE: print("You have run out of options") 
    elif search_state == SearchState.TARGET_REACHED: print("You have reached the target")

def find_path(actual_point, target_point, playground) -> SearchState:
    
    new_playground = playground

    return (Pipe(generate_possible_moves(actual_point))
             .then(check_all_moves_for_collision_and_distance(target_point, new_playground))
             .then(filter_feasible_moves)
             .then(select_next_move)
             .then(evaluate_next_progress(actual_point, target_point, new_playground))
             .flush())

def get_point_position(playground, point) -> tuple[int,int]:

    point_pos = tuple((i,j) for i, t in enumerate(playground) for j,k in enumerate(playground[i]) if playground[i][j] == point)
      
    return point_pos[0]

def command_line_interface() -> PlaygroundParameters:
    
    x_size = int(input("Entry x size of playground: "))
    y_size = int(input("Entry y size of playground: "))
    amount_of_obstacles = int(input("Entry amount of obstacles in playground: "))
    
    return PlaygroundParameters(x_size, y_size, amount_of_obstacles)

def generate_playground_based_on_used_interface():
    
    return (Pipe(command_line_interface())
             .then(generate_playground_with_obstacles)
             .flush())

def game_loop(*args) -> None:
    
    if (input("Play again? ")).lower() == "yes":
        clear()
        run_game()
    else:
        pass

def run_game():
    
    playground = generate_playground_based_on_used_interface()
    
    return (Pipe(find_path(get_point_position(playground, START), get_point_position(playground, TARGET), playground))
             .then(is_target_reached)
             .then(game_loop)
             .flush())

if __name__ == "__main__":
    
    run_game()
    
