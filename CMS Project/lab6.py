def solve_maze(maze):
    # Find the starting position of the hiker
    start_row, start_col = None, None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "P":
                start_row, start_col = row, col
                break
        if start_row is not None:
            break
    
    # Call the recursive helper function to solve the maze
    solved = solve_maze_helper(maze, start_row, start_col)
    
    # Return the status and path
    if solved:
        return "Solved", get_path(maze)
    else:
        return "Unsolved", None

def solve_maze_helper(maze, row, col):
    # Check if the current position is out of bounds or a barrier
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[row]) or maze[row][col] == "*":
        return False
    
    # Check if the current position is the mountain top
    if maze[row][col] == "T":
        return True
    
    # Mark the current position as visited
    maze[row][col] = "."
    
    # Recursively explore all possible directions
    if solve_maze_helper(maze, row - 1, col):  # Up
        return True
    if solve_maze_helper(maze, row + 1, col):  # Down
        return True
    if solve_maze_helper(maze, row, col - 1):  # Left
        return True
    if solve_maze_helper(maze, row, col + 1):  # Right
        return True
    
    # If no path is found, backtrack and mark the current position as unvisited
    maze[row][col] = " "
    return False

def get_path(maze):
    # Find the path from the starting position to the mountain top
    path = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == ".":
                path.append((row, col))
    return path

maze1 = [
    [" ", "", " ", "", " ", " "],
    [" ", "", " ", "", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
]

status, path = solve_maze(maze1)
print(status)
if status == "Solved":
    print("Path:", path)

maze2 = [
    [" ", "", " ", "", " ", " "],
    [" ", "", " ", "", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["", " ", "", "", "", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["", " ", " ", " ", " ", ""]
]

status, path = solve_maze(maze2)
print(status)
if status == "Solved":
    print("Path:", path)
