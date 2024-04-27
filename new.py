# def solve_maze(maze):
#     def is_valid(x, y):
#         return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] not in ('*', 'V')

#     def find_path(x, y, path):
#         if not is_valid(x, y):
#             return False
#         if maze[x][y] == 'T':
#             path.append((x, y))
#             return True
#         maze[x][y] = 'V'  # mark as visited
#         directions = [
#             (x, y + 1),  # right
#             (x, y - 1),  # left
#             (x + 1, y),  # down
#             (x - 1, y)   # up
#         ]
#         for dx, dy in directions:
#             if find_path(dx, dy, path):
#                 path.append((x, y))
#                 return True
#         return False

#     # Find the starting point (P)
#     for i in range(len(maze)):
#         for j in range(len(maze[0])):
#             if maze[i][j] == 'P':
#                 start_x, start_y = i, j
#                 break

#     path = []
#     if find_path(start_x, start_y, path):
#         path.reverse()
#         return "Solved", path
#     else:
#         return "Unsolved", []

# # Driver
# maze1 = [
#     [" ", "*", " ", "*", " ", " "],
#     [" ", "*", " ", "*", " ", " "],
#     ["P", " ", " ", " ", "*", " "],
#     ["*", " ", "*", "*", "*", " "],
#     [" ", " ", " ", " ", "*", "T"],
#     ["*", " ", " ", " ", " ", " "]
# ]

# status1, path1 = solve_maze(maze1)
# print(status1)
# if status1 == "Solved":
#     print("Path:", path1)

# maze2 = [
#     [" ", "*", " ", "*", " ", " "],
#     [" ", "*", " ", "*", " ", " "],
#     ["P", " ", " ", " ", "*", " "],
#     ["*", " ", "*", "*", "*", " "],
#     [" ", " ", " ", " ", "*", "T"],
#     ["*", " ", " ", " ", " ", "*"]
# ]

# status2, path2 = solve_maze(maze2)
# print(status2)
# if status2 == "Solved":
#     print("Path:", path2)


i=1
j=1

while i<10 or j<5:
    print(i)
    i+=1
    j+=1