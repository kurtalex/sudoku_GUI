board = [
    [0, 5, 0, 0, 2, 7, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [7, 0, 0, 1, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 1, 4],
    [0, 0, 0, 8, 0, 5, 0, 7, 0],
    [0, 3, 4, 0, 0, 0, 0, 5, 0],
    [0, 0, 3, 0, 1, 0, 0, 0, 6],
    [0, 0, 2, 9, 6, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0]
]


def solve(bo):
    # Solves a Sudoku board using a backtracking algorithm
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y + 3):
        for j in range(box_x * 3, box_x + 3):
            if bo[i][i] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- " * 14)
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row and col

    return None


print_board(board)
solve(board)
print("_" * 28)
print_board(board)
