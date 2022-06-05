from click import clear
from pymonad.reader import Pipe

from app import find_path, cli_input, generate_playground_with_obstacles
from app.types import PLaygroundMarks
from app.utils import get_point_position


def run_game():
    play_game = True
    while play_game:
        playground = generate_playground_with_obstacles(cli_input())
        find_path(
            get_point_position(playground, PLaygroundMarks.START),
            get_point_position(playground, PLaygroundMarks.TARGET),
            playground,
        )
        if (input("Play again? ")).lower() != "yes":
            break
        clear()


if __name__ == "__main__":
    run_game()
