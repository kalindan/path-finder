import random as rd
from typing_extensions import Self
from app.types import PlaygroundParameters, PLaygroundMarks


def generate_empty_playground(x_size, y_size) -> list[list[str]]:
    return [
        [PLaygroundMarks.OBSTACLE if i == 0 or i == x_size - 1 or j == 0 or j == y_size - 1 else PLaygroundMarks.EMPTY_POINT for i in range(x_size)]
        for j in range(y_size)
    ]


def add_obstacles_to_playground(number_of_obstacles, playground) -> list[list[str]]:
    new_playground = playground
    for _ in range(number_of_obstacles):
        new_playground[rd.randint(1, len(new_playground) - 2)][rd.randint(1, len(new_playground[0]) - 2)] = PLaygroundMarks.OBSTACLE
    return new_playground


def add_point_to_playground(point, playground) -> list[list[str]]:
    new_playground = playground
    new_playground[rd.randint(1, len(new_playground) - 2)][rd.randint(1, len(new_playground[0]) - 2)] = str(point)
    return new_playground


def generate_playground_with_obstacles(playground_parameters: PlaygroundParameters) -> list[list[str]]:
    empty_playground = generate_empty_playground(playground_parameters.x_size, playground_parameters.y_size)
    playground_with_obstacles = add_obstacles_to_playground(playground_parameters.amount_of_obstacles, empty_playground)
    playground_with_start = add_point_to_playground(PLaygroundMarks.START, playground_with_obstacles)
    playground_with_target = add_point_to_playground(PLaygroundMarks.TARGET, playground_with_start)
    return playground_with_target
