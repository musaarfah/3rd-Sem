def solve_maze(maze):
    def find_path(x, y, current_path):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == '*' or visited[x][y]:
            return False
        current_path.append((x, y))
        visited[x][y] = True
        if maze[x][y] == 'T':
            return True
        
        if (find_path(x + 1, y, current_path) or find_path(x - 1, y, current_path) or find_path(x, y + 1, current_path) or find_path(x, y - 1, current_path)):
            return True
        current_path.pop()
        return False

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    start_x=0
    start_y=0
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j]=='P':
                start_x=i
                start_y=j
                break

    path = []
    if find_path(start_x, start_y, path):
        return "Solved", path
    else:
        return "Unsolved", []

# Driver
maze1 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
]
status1, path1 = solve_maze(maze1)
print(status1)
if status1 == "Solved":
    print("Path:", path1)

maze2 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", "*"]
]
status2, path2 = solve_maze(maze2)
print(status2)
if status2 == "Solved":
    print("Path:", path2)
