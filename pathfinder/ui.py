from .types import PlaygroundParameters

def cli_input() -> PlaygroundParameters:
    x_size = int(input("Entry x size of playground: "))
    y_size = int(input("Entry y size of playground: "))
    amount_of_obstacles = int(input("Entry amount of obstacles in playground: "))
    return PlaygroundParameters(x_size, y_size, amount_of_obstacles)
