from click import clear
import numpy as np
import random as rd
import time

def generate_empty_playground(x_size, y_size):
    
    playground = np.full(shape=(x_size,y_size), fill_value=".")
    for index, row in enumerate(playground):
        for index_inner, column in enumerate(row):
            if index == 0 or index == x_size-1 or index_inner == 0 or index_inner == y_size-1:
                playground[index][index_inner] = "#"
                
    return playground

def generate_obstacles_at_playground(playground,number_of_obstacles):
    
    new_playground = playground
    for _ in range(number_of_obstacles):
        new_playground[rd.randint(1,len(new_playground)-2)][rd.randint(1,len(new_playground[0])-2)] = "#"

    return new_playground

def generate_point_at_playground(playground, point):
    
    new_playground = playground
    new_playground[rd.randint(1,len(new_playground)-2)][rd.randint(1,len(new_playground[0])-2)] = str(point)
    
    return new_playground

def generate_playground_with_obstacles(x_size, y_size, number_of_obstacles):
    
    empty_playground = generate_empty_playground(x_size, y_size)
    playground_with_obstacles = generate_obstacles_at_playground(empty_playground,number_of_obstacles)
    playground_with_obstacles_and_start = generate_point_at_playground(playground_with_obstacles, "S")
    playground_with_obstacles_start_and_target = generate_point_at_playground(playground_with_obstacles_and_start, "T")
    
    return playground_with_obstacles_start_and_target

def check_move_for_collision_and_distance(playground, direction):
    
    if playground[direction[0]][direction[1]] == "#" or playground[direction[0]][direction[1]] == "o":
        return 1000
    else:
        distance = np.abs(direction[0] - direction[2]) + np.abs(direction[1] - direction[3])
        return distance

def select_next_move(possible_moves_distance):
    
    min_distance = min(possible_moves_distance)
    if min_distance == 1000:
        return None
    else:
        direction = possible_moves_distance.index(min_distance)
        return direction

def paint_moved_step(playground, a_i, a_j):
    
    new_playground = playground
    if new_playground[a_i][a_j] != "T" and new_playground[a_i][a_j] != "S":
        new_playground[a_i][a_j] = "o"
        
    return new_playground

def find_path(a_i, a_j, t_i, t_j, playground):
    
    new_playground = playground
    
    move_up = (a_i-1,a_j,t_i,t_j)
    move_down = (a_i+1,a_j,t_i,t_j)
    move_left = (a_i,a_j-1,t_i,t_j)
    move_right = (a_i,a_j+1,t_i,t_j)
    possible_moves = (move_up, move_down, move_left, move_right)
    
    move_up_distance = check_move_for_collision_and_distance(new_playground, move_up)
    move_down_distance = check_move_for_collision_and_distance(new_playground, move_down)
    move_left_distance = check_move_for_collision_and_distance(new_playground, move_left)
    move_right_distance = check_move_for_collision_and_distance(new_playground, move_right)
    possible_moves_distance = (move_up_distance,move_down_distance, move_left_distance, move_right_distance)
    
    next_move = select_next_move(possible_moves_distance)
    
    if next_move !=  None: 
        new_playground = paint_moved_step(new_playground, a_i, a_j)
        print_playground(new_playground)
        
        if a_i == t_i and a_j == t_j:
             
             return print("You have reached the target")
         
        return  find_path(possible_moves[next_move][0], possible_moves[next_move][1], t_i, t_j, new_playground)
        
    return print("You have run out of options")

def print_playground(field):
    
    clear()
    extracted_row = ""
    for i,row in enumerate(field):
        for j, column in enumerate(row):
            extracted_row += field[i][j]
        print(extracted_row)
        extracted_row = ""
    time.sleep(0.2)

def get_point_position(playground, point):
    
    for i,t in enumerate(playground):
        for j,k in enumerate(playground[i]):
            if playground[i][j] == point:
                p_i = i
                p_j = j     
                
                return p_i, p_j

def main():
    
    x_size = int(input("Entry x size of playground: "))
    y_size = int(input("Entry y size of playground: "))
    amount_of_obstacles = int(input("Entry amount of obstacles in playground: "))
    
    playground = generate_playground_with_obstacles(x_size, y_size, amount_of_obstacles)
    
    s_i, s_j = get_point_position(playground, "S")
    t_i, t_j = get_point_position(playground, "T")   

    find_path(s_i, s_j, t_i, t_j, playground)

if __name__ == "__main__":
    
    while True:
        main()
        if (input("Play again? ")).lower() == "yes":
            clear()
            pass
        else:
            break
