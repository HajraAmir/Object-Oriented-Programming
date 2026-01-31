def solve_maze(maze):
    stack = []
    visited = set()
    start_row, start_col = None, None

    # Find the starting point
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                start_row, start_col = i, j
                break

    if start_row is None or start_col is None:
        return "Unsolved", []

    stack.append((start_row, start_col))

    while stack:
        current_row, current_col = stack.pop()
        visited.add((current_row, current_col))

        if maze[current_row][current_col] == "T":
            path = [(start_row, start_col)]  # Starting point
            # Reconstruct path by backtracking
            while (current_row, current_col) != (start_row, start_col):
                path.append((current_row, current_col))
                current_row, current_col = stack.pop()
            path.append((start_row, start_col))  # Add starting point
            path.reverse()  # Reverse to get correct order
            return "Solved", path

        # Explore all possible directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != "*" and (new_row, new_col) not in visited:
                stack.append((new_row, new_col))

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
