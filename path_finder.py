import enum
import numpy as np
import random as rd
import curses
from curses import wrapper
import time



def previous_iterations():

#  playground = np.array([["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
#                        ["#",".","T",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
#                        ["#",".","#","#","#",".",".",".","#","#","#",".",".",".",".",".",".","#"],
#                        ["#",".","#",".","#",".",".",".","#",".","#",".","#","#","#",".",".","#"],
#                        ["#",".","#","#","#",".",".",".","#","#","#",".","#",".","#",".",".","#"],
#                        ["#",".",".",".",".",".",".",".",".",".",".",".","#","#","#",".",".","#"],
#                        ["#",".","#","#","#",".",".","#","#","#",".",".",".",".",".",".",".","#"],
#                        ["#",".","#",".","#",".",".","#",".","#",".",".",".",".",".",".",".","#"],
#                        ["#",".","#","#","#",".",".","#","#","#",".","#","#","#",".",".",".","#"],
#                        ["#",".",".",".",".",".",".",".",".",".",".","#",".","#",".",".",".","#"],
#                        ["#",".",".",".",".",".","#",".",".",".",".","#","#","#",".",".",".","#"],
#                        ["#",".",".","#","#","#",".",".",".",".",".",".",".",".",".",".",".","#"],
#                        ["#",".",".","#",".","#",".",".",".",".",".",".",".",".",".",".",".","#"],
#                        ["#",".",".","#","#","#",".","#","#","#",".",".",".",".",".",".",".","#"],
#                        ["#",".",".",".",".",".",".","#",".","#","S",".",".",".",".",".",".","#"],
#                        ["#",".","#","#","#",".",".","#","#","#",".","#","#","#",".",".",".","#"],
#                        ["#",".","#",".","#",".",".",".",".",".",".","#",".","#",".",".",".","#"],
#                        ["#",".","#","#","#",".",".",".",".",".",".","#","#","#",".",".",".","#"],
#                        ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#"],
#                        ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]])    

# 1st iteration

# def move_up(a_i, a_j, t_i, t_j, field, test):
#     a_i_up = a_i - 1
#     if field[a_i_up][a_j] == "#" or field[a_i_up][a_j] == "o":
#         points = 10000
#     else:
#         points = np.abs(a_i_up - t_i) + np.abs(a_j - t_j)
#     if not test and field[a_i_up][a_j] != "T":
#         field[a_i_up][a_j] = "o"
#     return points, a_i_up, a_j, field

# def move_down(a_i, a_j, t_i, t_j, field, test):
#     a_i_down = a_i + 1
#     if field[a_i_down][a_j] == "#" or field[a_i_down][a_j] == "o":
#         points = 10000
#     else:
#         points = np.abs(a_i_down - t_i) + np.abs(a_j - t_j)
#     if not test and field[a_i_down][a_j] != "T":
#         field[a_i_down][a_j] = "o"
#     return points, a_i_down, a_j, field

# def move_left(a_i, a_j, t_i, t_j, field, test):
#     a_j_left = a_j - 1
#     if field[a_i][a_j_left] == "#" or field[a_i][a_j_left] == "o":
#         points = 10000
#     else:
#         points = np.abs(a_j_left - t_j) + np.abs(a_i - t_i)
#     if not test and field[a_i][a_j_left] != "T":
#         field[a_i][a_j_left] = "o"
#     return points, a_i, a_j_left, field

# def move_right(a_i, a_j, t_i, t_j, field, test):
#     a_j_right = a_j + 1
#     if field[a_i][a_j_right] == "#" or field[a_i][a_j_right] == "o":
#         points = 10000
#     else:
#         points = np.abs(a_j_right - t_j) + np.abs(a_i - t_i)
#     if not test and field[a_i][a_j_right] != "T":
#         field[a_i][a_j_right] = "o"
#     return points, a_i, a_j_right, field

# def move_step(a_i, a_j, t_i, t_j, field):
    
#     test = True
#     move_commands = [move_left, move_right, move_up, move_down]
    
#     move_points = 1000
#     for index, move in enumerate(move_commands):
#         points, a_i_test, a_j_test, field_test = move(a_i, a_j, t_i, t_j, field, test)
#         if points < move_points:
#             move_points = points
#             chosen_move = index

# 2nd iteration

#     if move_points == 1000:
#         no_choices = True
#     else:
#         no_choices = False
#         test = False
#         points, a_i, a_j, field = move_commands[chosen_move](a_i, a_j, t_i, t_j, field, test)
#     return a_i, a_j, field, no_choices

# def move(positions : list, field, test):
#     if field[positions[0]][positions[1]] == "#" or field[positions[0]][positions[1]] == "o":
#         points = 10000
#     else:
#         points = np.abs(positions[0] - positions[2]) + np.abs(positions[1] - positions[3])
#     if not test and field[positions[0]][positions[1]] != "T":
#         field[positions[0]][positions[1]] = "o"
#     return points, positions[0], positions[1], field

# def move_step(a_i, a_j, t_i, t_j, field):
    
#     test = True
#     pos_list = [[a_i-1,a_j,t_i,t_j],
#                 [a_i+1,a_j,t_i,t_j],
#                 [a_i,a_j-1,t_i,t_j],
#                 [a_i,a_j+1,t_i,t_j]]

#     move_points = 1000
#     for index in range(4):
#         points, a_i_test, a_j_test, field_test = move(pos_list[index], field, test)
#         if points < move_points:
#             move_points = points
#             chosen_move = index

#     if move_points == 1000:
#         no_choices = True
#     else:
#         no_choices = False
#         test = False
#         points, a_i, a_j, field = move(pos_list[chosen_move], field, test)
#     return a_i, a_j, field, no_choices
    pass

def generate_playground(size, number_of_obstacles):
    
    x_size = size
    y_size = size * 2

    playground = np.full(shape=(x_size,y_size), fill_value=".")
    for index, row in enumerate(playground):
        for index_inner, column in enumerate(row):
            if index == 0 or index == x_size-1 or index_inner == 0 or index_inner == y_size-1:
                playground[index][index_inner] = "#"

    for _ in range(number_of_obstacles):
        playground[rd.randint(1,x_size-2)][rd.randint(1,y_size-2)] = "#"

    playground[rd.randint(1,x_size-2)][rd.randint(1,y_size-2)] = "T"
    playground[rd.randint(1,x_size-2)][rd.randint(1,y_size-2)] = "S"
    return playground

def move_step(a_i, a_j, t_i, t_j, field):
    
    pos_list = np.array([[a_i-1,a_j,t_i,t_j],  # move up
                         [a_i+1,a_j,t_i,t_j],  # move down
                         [a_i,a_j-1,t_i,t_j],  # move left
                         [a_i,a_j+1,t_i,t_j]]) # move right
    move_points = 1000

    for index in range(4):
        if field[pos_list[index][0]][pos_list[index][1]] == "#" or field[pos_list[index][0]][pos_list[index][1]] == "o":
            points = 10000
        else:
            points = np.abs(pos_list[index][0] - pos_list[index][2]) + np.abs(pos_list[index][1] - pos_list[index][3])
        if points < move_points:
            move_points = points
            chosen_move = index

    if move_points == 1000:
        no_choices = True
        chosen_move = 0
    else:
        no_choices = False
        if field[pos_list[chosen_move][0]][pos_list[chosen_move][1]] != "T":
            field[pos_list[chosen_move][0]][pos_list[chosen_move][1]] = "o"

    return pos_list[chosen_move][0], pos_list[chosen_move][1], field, no_choices

def print_playground(field, stdscr):
    
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)

    stdscr.clear()
    for i,row in enumerate(field):
        for j, column in enumerate(row):
            stdscr.addstr(i,j*2,column, blue_and_black)
    stdscr.refresh()
    time.sleep(0.2)

def find_path(field, stdscr):

    for i,t in enumerate(field):
        for j,k in enumerate(field[i]):
            if field[i][j] == "S":
                s_i = i
                s_j = j 
            elif field[i][j] == "T":
                t_i = i
                t_j = j 
   
    a_i = s_i # actual position Y
    a_j = s_j # actual position X

    target_reached = False
    while not target_reached:
        if a_i == t_i and a_j == t_j:
            target_reached = True
        else:
            a_i, a_j, field, no_choices = move_step(a_i, a_j, t_i, t_j, field)
            print_playground(field, stdscr)
            if no_choices:
                print("Run out of choices")
                break

def main(stdscr):

    find_path(generate_playground(18,50), stdscr)
    stdscr.getch()

if __name__ == "__main__":
    wrapper(main)
    
