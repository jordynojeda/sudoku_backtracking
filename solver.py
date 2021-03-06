
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(the_board):
  
    find = find_empty(the_board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if valid(the_board,i, (row,column)):
            the_board[row][column] = i

            if solve(the_board):
                return True

            the_board[row][column] = 0

    return False

def valid(the_board, number, position):

    # Check row
    for i in range(len(the_board[0])):
        if the_board[position[0]][i] == number and position[1] != i:
            return False

    # Check Column
    for i in range(len(the_board)):
        if the_board[i][position[1]] == number and position[0] != i:
            return False

    # Check 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if the_board[i][j] == number and (i,j) != position:
                return False

    return True


def print_board(the_board):

    for i in range(len(the_board)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - -  ")

        for j in range(len(the_board[0])):
            if j == 0:
                print("| ", end="")

            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(the_board[i][j]) + " |")

            else:
                print(str(the_board[i][j]) + " ", end="")

def find_empty(the_board):
    for i in range(len(the_board)):
        for j in range(len(the_board[0])):
            if the_board[i][j] == 0:
                return(i,j)  # row, column

    return None

print_board(board)
solve(board)
print("")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("")
print_board(board)

