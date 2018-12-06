team = [",","w","b"]
symbol = [" ", "1", "B", "N", "R", "Q", "K"]#[")","S","c","C"]

def printBoard(board,board2):
    y = -1
    for x in range (25):
        a = " "
        if x % 3 == 0:
            print(" +-----+-----+-----+-----+-----+-----+-----+-----+")
        elif (x-1) % 3 == 0:
            y += 1
            print(" | ",symbol[board[y][0]]," | ",symbol[board[y][1]],
                  " | ",symbol[board[y][2]]," | ",symbol[board[y][3]],
                  " | ",symbol[board[y][4]]," | ",symbol[board[y][5]],
                  " | ",symbol[board[y][6]]," | ",symbol[board[y][7]]," |")
        else:
            print(" |", team[board2[y][0]],"  |",team[board2[y][1]],
                  "  |",team[board2[y][2]],"  |",team[board2[y][3]],
                  "  |",team[board2[y][4]],"  |",team[board2[y][5]],
                  "  |",team[board2[y][6]],"  |",team[board2[y][7]],"  |")
    pass

def markBoard(board,board2,row,col,piece,player):
    if board2[row][col] != player:
        board2[row][col] = player
        board[row][col] = piece
    else:
        print("space is already occupied.")
    pass

def getPlayerMove(board,board2,player):
    while True:
        pr=int(input("pieces row"))
        pc=int(input("pieces column"))
        if board2[pr][pc] != player:
            print("you cannot use that piece!")
        else:        
            p = board[pr][pc]
            break
    moves = lglmvs(p, pr, pc, player, team)
    while True:
        try:
            r=int(input("new row"))
            c=int(input("new column"))
            newloc = (r, c)
            if newloc in moves:
                board[pr][pc] = 0
                board2 [pr][pc] = 0
                return (r,c, p)
        except:
            print ("invalid!")

def hasKings(board):
    m = 0
    for row in board:
        for space in row:
            if space == 6:
                m = m + 1
    if m == 2:
        return True
    else:
        return False

def lglmvs(piece, cx, cy, player, team):
    moves=["cancel"]
    print (cx,cy)
    if piece == 1:
        moves.append(Pawn(cx,cy,moves, team, player))
    elif piece == 2:
        moves.append(Bishop(cx,cy,moves, team))
    elif piece == 3:
        moves.append(Knight(cx,cy,moves, team))
    elif piece == 4:
        moves.append(Rook(cx,cy,moves, team))
    elif piece == 5:
        moves.append(Rook(cx,cy,moves, team) + Bishop(cx,cy,moves, team))
    elif piece == 6:
        moves.append(King(cx,cy,moves, team))
    return moves

def Pawn (cx, cy, moves, team, player):
    i = -1**int(player)
    if validspace(cx+i,cy+1, team) == "Enemy":
        moves.append((nx, ny))
    if validspace(cx+i,cy-1, team) == "Enemy":
        moves.append((nx, ny))
    if validspace(cx+i,cy, team) == True:
        moves.append((nx, ny))
    return moves

def King (cx, cy, moves, team):
    if validspace(cx+1,cy+1, team) == "Enemy" or  validspace(cx+1,cy+1, team) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy+1, team) == "Enemy" or  validspace(cx-1,cy+1, team) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy-1, team) == "Enemy" or  validspace(cx+1,cy-1, team) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy-1, team) == "Enemy" or  validspace(cx-1,cy-1, team) == True:
        moves.append((nx, ny))
    if validspace(cx,cy+1, team) == "Enemy" or  validspace(cx,cy+1, team) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy, team) == "Enemy" or  validspace(cx-1,cy, team) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy, team) == "Enemy" or  validspace(cx+1,cy, team) == True:
        moves.append((nx, ny))
    if validspace(cx,cy-1, team) == "Enemy" or  validspace(cx,cy-1, team) == True:
        moves.append((nx, ny))
    for (nx,ny) in moves:
        if checktest(cx, cy, nx, ny, team) == True:
            del moves[i + 1]
    return moves

def Knight (cx, cy, moves, team):
    if validspace(cx+1,cy+2, team) == "Enemy" or  validspace(cx+1,cy+2, team) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy+2, team) == "Enemy" or  validspace(cx-1,cy+2, team) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy-2, team) == "Enemy" or  validspace(cx+1,cy-2, team) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy-2, team) == "Enemy" or  validspace(cx-1,cy-2, team) == True:
        moves.append((nx, ny))
    if validspace(cx+2,cy+1, team) == "Enemy" or  validspace(cx+2,cy+1, team) == True:
        moves.append((nx, ny))
    if validspace(cx-2,cy+1, team) == "Enemy" or  validspace(cx-2,cy+1, team) == True:
        moves.append((nx, ny))
    if validspace(cx+2,cy-1, team) == "Enemy" or  validspace(cx+2,cy-1, team) == True:
        moves.append((nx, ny))
    if validspace(cx-2,cy-1, team) == "Enemy" or  validspace(cx-2,cy-1, team) == True:
        moves.append((nx, ny))
    return moves
 
def Bishop (cx, cy, moves, team):
    for i in range (cx, 7):
        if validspace(i, cy+i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy+i, team) == True:
            moves.append((nx, ny))
        elif validspace(i, cy+i, team) == False:
            break
    for i in range (cx, 0, -1):
        if validspace(i, cy-i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy-i, team) == True:
            moves.append((nx, ny))
        elif validspace(i, cy-i, team) == False:
            break
    for i in range (cy, 7):
        if validspace(cx-i, i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx-i, i, team) == True:
            moves.append((nx, ny))
        elif validspace(cx-i, i, team) == False:
            break
    for i in range (cy, 0, -1):
        if validspace(cx+i, i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx+i, i, team) == True:
            moves.append((nx, ny))
        elif validspace(cx+i, i, team) == False:
            break
    return moves

def Rook(cx,cy, moves, team):
    for i in range (cx, 7):
        if validspace(i, cy, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy, team) == True:
            moves.append((nx, ny))
        elif validspace(i, cy, team) == False:
            break
    for i in range (cx, 0, -1):
        if validspace(i, cy, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy, team) == True:
            moves.append((nx, ny))
        elif validspace(i, cy, team) == False:
            break
    for i in range (cy, 7):
        if validspace(cx, i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx, i, team) == True:
            moves.append((nx, ny))
        elif validspace(cx, i, team) == False:
            break
    for i in range (cy, 0, -1):
        if validspace(cx, i, team) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx, i, team) == True:
            moves.append((nx, ny))
        elif validspace(cx, i, team) == False:
            break
    return moves
    
def validspace(nx, ny, team):
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        return False
    elif team[nx][ny] == 0:
        return True
    elif team [nx][ny] == player:
        return False
    elif team[nx][ny] != player:
        return "Enemy"
        
def checktest(cx, cy, nx, ny, team):
    tests = team[cx][cy] % 2 + 1
    for i in board2[row][col]:
        if board2[row][col] == tests:
            dsquares = lglmvs(board[row][col], row, col)
    if (nx,ny) in dsquares:
        return True
    else:
        return False
    

def main():
    board = [[4,3,2,5,6,2,3,4],
             [1,1,1,1,1,1,1,1],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [1,1,1,1,1,1,1,1],
             [4,3,2,5,6,2,3,4]]
    
    board2 = [[2,2,2,2,2,2,2,2],
              [2,2,2,2,2,2,2,2],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1]]
    player = 1
    while hasKings(board):
        printBoard(board,board2)
        row,col,piece = getPlayerMove(board,board2,player)
        markBoard(board,board2,row,col,piece,player)
        player = player % 2 + 1 
    printBoard(board,board2)
    player = player % 2 + 1
    print ("player "+str(player)+" wins!")
main()

##############################################################################

#card table (future)
    #GhostForm
    #Wololo
    #Charge
    #RoyalMarriage
    #Resurection
    #Archery
    #Knighting
    #Draft
    #Faith
    #Rookerie
    #SummonDragon
    #Teleport
    #Chivalry
    



