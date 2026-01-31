def solve_maze(maze):
    def dfs(row, col, path):
        if not (0 <= row < len(maze) and 0 <= col < len(maze[0])) or maze[row][col] == "*":
            return False

        if maze[row][col] == "T":
            return True

        if (row, col) in visited:
            return False

        visited.add((row, col))
        path.append((row, col))

        # Explore all possible directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(row + dr, col + dc, path):
                return True

        # Backtrack if no path found
        path.pop()
        return False

    visited = set()
    path = []
    start_row, start_col = None, None

    # Find the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                start_row, start_col = i, j
                break

    if dfs(start_row, start_col, path):
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
status, path = solve_maze(maze1)
print(status)
if status == "Solved":
    print("Path:", path)

maze2 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", "*"]
]
status, path = solve_maze(maze2)
print(status)
if status == "Solved":
    print("Path:", path)
