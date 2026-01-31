def solve_maze(maze):
    start_row, start_col = None, None

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                start_row, start_col = i, j
                break

    if start_row is None or start_col is None:
        return "Unsolved", []

    stack = [(start_row, start_col, [(start_row, start_col)])]
    visited = set([(start_row, start_col)])

    while stack:
        row, col, path = stack.pop()
        if maze[row][col] == "T":
            return "Solved", path

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) \
                    and maze[new_row][new_col] != "*" \
                    and (new_row, new_col) not in visited:
                new_path = path + [(new_row, new_col)]
                stack.append((new_row, new_col, new_path))
                visited.add((new_row, new_col))

    return "Unsolved", []

maze1 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
]

maze2 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", "*"]
]

status1, path1 = solve_maze(maze1)
print(status1)
if status1 == "Solved":
    print("Path:", path1)

status2, path2 = solve_maze(maze2)
print(status2)
if status2 == "Solved":
    print("Path:", path2)
