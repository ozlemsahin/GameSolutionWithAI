

player1 = 'x' #maximizer
player2 = 'o' #minimizer
board = [['x', 'o', 'x'],
          ['o', '_', '_'],
          ['_', '_', '_']]
depth = 0
    
#is there any moves left?
def isMovesLeft(board):
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False

#give score 
def evaluate(board):
    
    #check rows for X
    rowScoreX=0
    for col in range(0,3):
        for row in range(0,3):
            if(board[col][row] == 'x'):
                
                rowScoreX = rowScoreX + 1
                #("row: "+ str(row) + " col: " + str(col) + " score: " +str(rowScoreX))
        if (rowScoreX == 3):
            return 10
        else:
            rowScoreX = 0

    #check rows for O
    rowScoreO=0
    for col in range(0,3):
        for row in range(0,3):
            if(board[col][row] == 'o'):
                rowScoreO = rowScoreO + 1
                #print("row: "+ str(row) + " col: " + str(col) + " score: " +str(rowScoreO))
        if (rowScoreO == 3):
            return -10
        else:
            rowScoreO = 0

    #check columns for X
    colScoreX=0
    for row in range(0,3):
        for col in range(0,3):
            if(board[col][row] == 'x'):
                colScoreX = colScoreX + 1
                #print("row: "+ str(row) + " col: " + str(col) + " score: " +str(colScoreX))
        if (colScoreX == 3):
            return 10
        else:
            colScoreX = 0



    #check columns for O
    colScoreO=0
    for row in range(0,3):
        for col in range(0,3):
            if(board[col][row] == 'o'):
                colScoreO = colScoreO + 1
                #print("row: "+ str(row) + " col: " + str(col) + " score: " +str(colScoreO))
        if (colScoreO == 3):
            return -10
        else:
            colScoreO = 0

    #check diagonals for X
    diaScoreX=0
    for row in range(0,3):
        if(board[row][row] == 'x'):
             diaScoreX = diaScoreX + 1
             #print("row: "+ str(row) + " col: " + str(row) + " score: " +str(diaScoreX))
    if (diaScoreX == 3):
        return 10
    else:
       diaScoreX = 0
        
    #check diagonals for O
    diaScoreO=0
    for row in range(0,3):
        if(board[row][row] == 'o'):
             diaScoreO = diaScoreO + 1
             #print("row: "+ str(row) + " col: " + str(row) + " score: " +str(diaScoreO))
    if (diaScoreO == 3):
        return -10
    else:
        diaScoreO = 0

    #check diagonals for X REVERSE
    diaScoreX=0
    for row in range(0,3):
        if(board[2-row][row] == 'x'):
             diaScoreX = diaScoreX + 1
             #print("row: "+ str(row) + " col: " + str(row) + " score: " +str(diaScoreX))
    if (diaScoreX == 3):
        return 10
    else:
       diaScoreX = 0


    #check diagonals for O REVERSE
    diaScoreO=0
    for row in range(0,3):
        if(board[2-row][row] == 'o'):
             diaScoreO = diaScoreO + 1
             #print("row: "+ str(row) + " col: " + str(row) + " score: " +str(diaScoreO))
    if (diaScoreO == 3):
        return -10
    else:
        diaScoreO = 0
        
        
        
    return 0

def minimax(board, isMaximizingPlayer):
    global depth
    
    #if ended
    score = evaluate(board)
    if(score == 10):
        return score
    if(score == -10):
        return score
    if(isMovesLeft(board) == False):
        return 0
    
    if(isMaximizingPlayer):
        bestValue = -1000
        
        #give all posibilities
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = 'x'
                    value = minimax(board,  False)
                    depth = depth + 1
                    bestValue = max(value, bestValue)
                    #undo move
                    board[i][j] = '_'        
        return bestValue
    
    else:
         bestValue = 1000
         
         for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = 'o'
                    value = minimax(board, False)
                    depth = depth + 1
                    bestValue = min(value, bestValue)
                    #undo move
                    board[i][j] = '_'        
         return bestValue
    
    
    
        
#begin
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    
    for i in range(3) :    
        for j in range(3) :
            if (board[i][j] == '_') :
                
                board[i][j] = player1
                moveVal = minimax(board, False)
                # Undo move
                board[i][j] = '_'

                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
    print("how many calculation happened: " + str(depth))
    return bestMove


print(findBestMove(board))



