
# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Alexander White
# Created: 2018-11-09
symbol = [ " ", "x", "o" ]

def printRow(row):
    # initialize output to the left border
    # for each square in the row...
        # add to output the symbol for this square followed by a border
    # print the completed output for this row
    pass

def printBoard(board):
    y = -1
    for x in range (7):
        a = " "
        if x % 2 == 0:
            print("+---+---+---+")
        else:
            y += 1
            print("|",symbol[board[y][0]],"|",symbol[board[y][1]],"|",symbol[board[y][2]],"|")
    pass

def markBoard(board, row, col, player):
    if board[row][col] == 0:
        board[row][col] = player
    else:#boolean, step 2c
        print("space is already occupied.")
    pass

def getPlayerMove():
    r=int(input("row"))
    c=int(input("column"))
    return (r,c)#tuple

def hasBlanks(board):
    m = 0
    for row in board:
        for space in row:
            if space == 0:
                m = m + 1
    if m > 0:
        return True
    else:
        return False


def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
