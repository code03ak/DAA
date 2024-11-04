def printSolution(board, N):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def isSafe(board, row, col, N):
    # Check this row on the left side
    if any(board[row][i] == 1 for i in range(col)):
        return False

    # Check upper diagonal on the left side
    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check lower diagonal on the left side
    if any(board[i][j] == 1 for i, j in zip(range(row, N), range(col, -1, -1))):
        return False

    return True

def solveNQUtil(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def solveNQ(N):
    board = [[0] * N for _ in range(N)]
    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
    else:
        printSolution(board, N)

# Driver Code
if __name__ == '__main__':
    N = int(input("Enter the size of the board: "))
    solveNQ(N)
