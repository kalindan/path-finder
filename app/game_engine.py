from typing import Iterator
import numpy as np
from functools import reduce

from app.types import PossibleMove, PLaygroundMarks
from app.playground_printer import print_playground_with_current_move

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

RIDICULOUSLY_BIG_DISTANCE = 10000


def generate_possible_moves(actual_point) -> Iterator[PossibleMove]:
    return (
        PossibleMove(
            move_in_x=actual_point[0] + direction[0],
            move_in_y=actual_point[1] + direction[1],
        )
        for direction in DIRECTIONS
    )


def is_move_in_collision(
    playground,
    move: PossibleMove,
) -> PossibleMove:
    if (
        playground[move.move_in_x][move.move_in_y] == PLaygroundMarks.OBSTACLE
        or playground[move.move_in_x][move.move_in_y] == PLaygroundMarks.PASSED_ROAD
    ):
        return PossibleMove(move.move_in_x, move.move_in_y, 0, is_in_collision=True)
    return move


def get_distance_from_target(target_point, move: PossibleMove) -> PossibleMove:
    distance = np.abs(move.move_in_x - target_point[0]) + np.abs(move.move_in_y - target_point[1])
    return PossibleMove(move.move_in_x, move.move_in_y, distance, move.is_in_collision)


def check_move_for_collision_and_distance(move: PossibleMove, target_point, playground) -> PossibleMove:
    collision_checked_move = is_move_in_collision(playground, move)
    distance_checked_move = get_distance_from_target(target_point, collision_checked_move)
    return distance_checked_move


def check_all_moves_for_collision_and_distance(target_point, playground, possible_moves: Iterator[PossibleMove]) -> Iterator[PossibleMove]:
    return (check_move_for_collision_and_distance(move, target_point, playground) for move in possible_moves)


def filter_feasible_moves(
    checked_moves: Iterator[PossibleMove],
) -> Iterator[PossibleMove]:
    return filter(lambda x: x.is_in_collision == False, checked_moves)


def select_next_move(filtered_moves: Iterator[PossibleMove]) -> PossibleMove | None:
    try:
        next_move: PossibleMove = reduce(
            lambda x, y: x if x.distance < y.distance else y,
            filtered_moves,
            PossibleMove(None, None, distance=RIDICULOUSLY_BIG_DISTANCE),
        )
        return next_move
    except:
        return None


def evaluate_next_progress(actual_point, target_point, playground, next_move: PossibleMove | None) -> None:
    if next_move == None:
        return print("You have run out of options")
    print_playground_with_current_move(actual_point, playground, PLaygroundMarks)
    if next_move.distance == 0:
        return print("You have reached the target")
    return find_path((next_move.move_in_x, next_move.move_in_y), target_point, playground)


def find_path(actual_point, target_point, playground) -> None:
    new_playground = playground
    possible_moves = generate_possible_moves(actual_point)
    checked_moves = check_all_moves_for_collision_and_distance(target_point, new_playground, possible_moves)
    filtered_moves = filter_feasible_moves(checked_moves)
    evaluate_next_progress(actual_point, target_point, new_playground, select_next_move(filtered_moves))
