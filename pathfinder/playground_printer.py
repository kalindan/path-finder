from click import clear
import time
from functools import reduce

DELAY = 0.05

def print_current_move(actual_point, playground, plg_marks) -> list[list[str]]:   
    new_playground = playground
    if new_playground[actual_point[0]][actual_point[1]] != plg_marks.TARGET and new_playground[actual_point[0]][actual_point[1]] != plg_marks.START:
        new_playground[actual_point[0]][actual_point[1]] = plg_marks.PASSED_ROAD     
    return new_playground

def print_playground(playground) -> None: 
    clear()
    [print(reduce(lambda x, y: x + y, row)) for row in playground]
    time.sleep(DELAY)

def print_playground_with_current_move(actual_point, playground, plg_marks) -> None: 
    print_playground(print_current_move(actual_point, playground, plg_marks))
