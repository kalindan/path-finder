def get_point_position(playground, point) -> tuple[int,int]:
    point_pos = tuple((i,j) for i, t in enumerate(playground) for j,k in enumerate(playground[i]) if playground[i][j] == point)
    return point_pos[0]