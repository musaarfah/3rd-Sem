def solve_maze(maze):
    visited = []
    for i in range(len(maze)):
        visited_row = []
        for j in range(len(maze[0])):
            visited_row.append(False)
        visited.append(visited_row)
    
    start_x, start_y = 0, 0
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'P':
                start_x, start_y = i, j
                break
    
    stack = [(start_x, start_y, [])]
    
    while stack:
        x, y, path = stack.pop()
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == '*' or visited[x][y]:
            continue
        
        path.append((x, y))
        visited[x][y] = True
        
        if maze[x][y] == 'T':
            return "Solved", path
        
        stack.append((x + 1, y, path[:]))
        stack.append((x - 1, y, path[:]))
        stack.append((x, y + 1, path[:]))
        stack.append((x, y - 1, path[:]))
    
    return "Unsolved", []


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
