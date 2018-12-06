#determines symbols
team = [",","w","b"]
symbol = [" ", "1", "B", "N", "R", "Q", "K"]#[")","S","c","C"]

def printBoard(board,board2):
    #this function renders the graphics
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
            print(" |",team[board2[y][0]],"  |",team[board2[y][1]],
                  "  |",team[board2[y][2]],"  |",team[board2[y][3]],
                  "  |",team[board2[y][4]],"  |",team[board2[y][5]],
                  "  |",team[board2[y][6]],"  |",team[board2[y][7]],"  |")
    pass

def markBoard(board,board2,row,col,piece,player):
    #might delete, could end up redundant
    if board2[row][col] != player:
        board2[row][col] = player
        board[row][col] = piece
    else:
        print("space is already occupied.")
    pass

def getPlayerMove(board,board2,player):
    #select piece
    while True:
        pr=int(input("pieces row"))
        pc=int(input("pieces column"))
        if board2[pr][pc] != player:
            print("you cannot use that piece!")
        else:        
            p = board[pr][pc]
            break
    #select new location for piece
    r=int(input("new row"))     #lglmvs(p, pr, pc)
    c=int(input("new column"))
    board[pr][pc] = 0
    board2 [pr][pc] = 0
    #check if move is valid
    return (r,c, p)#tuple

def hasKings(board):
    #check for victory conditions
    #might add check/checkmate function later
    m = 0
    for row in board:
        for space in row:
            if space == 6:
                m = m + 1
    if m == 2:
        return True
    else:
        return False

def lglmvs(piece, cx, cy):
    moves["cancel"]
    if piece == 1:
        moves.append(Pawn(cx,cy,moves))
    elif piece == 2:
        moves.append(Bishop(cx,cy,moves))
    elif piece == 3:
        moves.append(Knight(cx,cy,moves))
    elif piece == 4:
        moves.append(Rook(cx,cy,moves))
    elif piece == 5:
        moves.append(Rook(cx,cy,moves) + Bishop(cx,cy,moves))
    elif piece == 6:
        moves.append(King(cx,cy,moves))

def Pawn (cx, cy):
    i = -1**(team [cx][cy])
    if validspace(cx+i,cy+1) == "Enemy":
        moves.append((nx, ny))
    if validspace(cx+i,cy-1) == "Enemy":
        moves.append((nx, ny))
    if validspace(cx+i,cy) == True:
        moves.append((nx, ny))
    return moves

def King (cx, cy):
    #determines which moves are readily available. 
    if validspace(cx+1,cy+1) == "Enemy" or  validspace(cx+1,cy+1) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy+1) == "Enemy" or  validspace(cx-1,cy+1) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy-1) == "Enemy" or  validspace(cx+1,cy-1) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy-1) == "Enemy" or  validspace(cx-1,cy-1) == True:
        moves.append((nx, ny))
    if validspace(cx,cy+1) == "Enemy" or  validspace(cx,cy+1) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy) == "Enemy" or  validspace(cx-1,cy) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy) == "Enemy" or  validspace(cx+1,cy) == True:
        moves.append((nx, ny))
    if validspace(cx,cy-1) == "Enemy" or  validspace(cx,cy-1) == True:
        moves.append((nx, ny))
    for (nx,ny) in moves:
        if checktest(cx, cy, nx, ny) == True:
            del moves[i + 1]
    return moves

def Knight (cx, cy):
    #determines which moves are readily available. 
    if validspace(cx+1,cy+2) == "Enemy" or  validspace(cx+1,cy+2) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy+2) == "Enemy" or  validspace(cx-1,cy+2) == True:
        moves.append((nx, ny))
    if validspace(cx+1,cy-2) == "Enemy" or  validspace(cx+1,cy-2) == True:
        moves.append((nx, ny))
    if validspace(cx-1,cy-2) == "Enemy" or  validspace(cx-1,cy-2) == True:
        moves.append((nx, ny))
    if validspace(cx+2,cy+1) == "Enemy" or  validspace(cx+2,cy+1) == True:
        moves.append((nx, ny))
    if validspace(cx-2,cy+1) == "Enemy" or  validspace(cx-2,cy+1) == True:
        moves.append((nx, ny))
    if validspace(cx+2,cy-1) == "Enemy" or  validspace(cx+2,cy-1) == True:
        moves.append((nx, ny))
    if validspace(cx-2,cy-1) == "Enemy" or  validspace(cx-2,cy-1) == True:
        moves.append((nx, ny))
    return moves


    
def Bishop (cx, cy):
    #determines which moves are readily available. 
    for i in range (cx, 7):
        if validspace(i, cy+i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy+i) == True:
            moves.append((nx, ny))
        elif validspace(i, cy+i) == False:
            break
    for i in range (cx, 0, -1):
        if validspace(i, cy-i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy-i) == True:
            moves.append((nx, ny))
        elif validspace(i, cy-i) == False:
            break
    for i in range (cy, 7):
        if validspace(cx-i, i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx-i, i) == True:
            moves.append((nx, ny))
        elif validspace(cx-i, i) == False:
            break
    for i in range (cy, 0, -1):
        if validspace(cx+i, i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx+i, i) == True:
            moves.append((nx, ny))
        elif validspace(cx+i, i) == False:
            break
    return moves




def Rook(cx,cy):
    #determines which moves are readily available. 
    for i in range (cx, 7):
        if validspace(i, cy) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy) == True:
            moves.append((nx, ny))
        elif validspace(i, cy) == False:
            break
    for i in range (cx, 0, -1):
        if validspace(i, cy) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(i, cy) == True:
            moves.append((nx, ny))
        elif validspace(i, cy) == False:
            break
    for i in range (cy, 7):
        if validspace(cx, i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx, i) == True:
            moves.append((nx, ny))
        elif validspace(cx, i) == False:
            break
    for i in range (cy, 0, -1):
        if validspace(cx, i) == "Enemy":
            moves.append((nx, ny))
            break
        elif validspace(cx, i) == True:
            moves.append((nx, ny))
        elif validspace(cx, i) == False:
            break
    return moves
    
def validspace(nx, ny):
    #determines whether a space is valid by seeing what is in the space
    #space doesn't exist
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        return False
    #space empty
    elif team[nx][ny] == 0:
        return True
    #space allied to player
    elif team [nx][ny] == player:
        return False
    #space enemy of player 
    elif team[nx][ny] != player:
        return "Enemy"
        
def checktest(cx, cy, nx, ny):
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
        player = player % 2 + 1 # switch player for next turn
    printBoard(board,board2)
    player = player % 2 + 1 # switch player for next turn
    print ("player "+str(player)+" wins!")
main()

##############################################################################

class Chess_Board:
    def __init__(self):
        #Initialise a new chess board.
        self.board = [['.']*8 for i in range(8)]
        board[7][4] = 'K'
        board[7][3] = 'Q'
        board[7][2] = 'B'
        board[7][1] = 'N'
        board[7][0] = 'R'

    def move(self, piece, x, y):
         #Reset the old spot to be empty then update the new spot
         self.board[piece.x][piece.y] = '.'
         self.board[x][y] = piece.symbol

         #Now that it's moved, update the piece itself
         piece.x = x
         piece.y = y

class Chess_Piece:
    #comtent
    x = 1        
    


#class King(Chess_Piece, team):

    #legal move set [x+a,y],[x+a,y+a],
    #               [x,y+a],[x-a,y+a]
    #
    #a = +- 1,
    #
    #castle = rook can move onto king space,
    #         rook has not moved,
    #         king has not moved,
    #         king is not in check,
    #         king will not be placed in or cross check
    #if castling, a = +- 2, then move rook behind where he moves
    #
    #cannot move into check.
    #cannot remain in check.
    #if neither of these rules can be sustained, opponent wins.
    

#class Queen(Chess_Piece, team):
    #legal move set [x+a,y],[x+a,y+a],
    #               [x,y+a],[x-a,y+a]
    #a = +- any integer

#class Rook(Chess_Piece, team):
    
    #legal move set [x+a,y],
    #               [x,y+a]
    #a = +- any integer


#class Bishop(Chess_Piece, team):

    #legal move set [x+a,y+a],
    #               [x-a,y+a]
    #a = +- any integer

#class Knight(Chess_Piece, team):

    #legal move set [x+a,y+b],[x+a,y-b]
    #a = +- 1 or +- 2
    #if abs(a) == 1, b = 2
    #if abs(a) == 2, b = 1
    #can pass other units

#class Pawn(Chess_Piece, team):

    #legal move set [x,y+a],
    #if first move  [x,y+2*a],
    #if capture or en passant [x+a,y+a],[x-a,y+a]
    #a = 1 if P1
    #a = -1 if P2
    #en passent = enemy pawn just used double forward,
    #             your pawn can capture the space passed,
    #             enemy pawn captured.

#class Checker(Chess_Piece, team):

    #legal move set [x+a,y+a],[x-a,y+a]
    #a = 1 if P1
    #a = -1 if P2
    #if blocked and P1, a = 2 and capture piece at a = 1,
    #if blocked and P2, a = -2 and capture piece at a = -1,
    #after capturing, check if other pieces are able to be captured using these moves.

#class Checker_King(Chess_Piece, team):
    
    #legal move set [x+a,y+a],[x-a,y+a]
    #a = +- 1
    #if capturing, a = +- 2,
    #after capturing, check if other pieces are able to be captured using these moves.
    
#class Archer(Chess_Piece, team):
    

#class Dragon(Chess_Piece, team):

    
#card table
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
    



