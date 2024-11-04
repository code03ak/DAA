def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col, n):
    # Base case: all queens are placed
    if col >= n:
        return True
    
    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            # Recursively place the remaining queens
            if solve_nqueens_util(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack if placing queen doesn't lead to a solution
    
    return False

def solve_nqueens(n):
    # Initialize the board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Place the first Queen at a position (e.g., (0,0))
    board[0][0] = 1
    
    # Use backtracking to place the remaining queens, starting from column 1
    if not solve_nqueens_util(board, 1, n):
        print("No solution exists")
    else:
        print("Final N-Queens Solution Matrix:")
        print_board(board)

# Get user input for the size of the board
n = int(input("Enter the size of the board (N): "))
solve_nqueens(n)
