import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentplayer = "X"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] +" | "+ board[1]+" | "+ board[2])
    print("-----------")
    print(board[3] +" | "+ board[4]+" | "+ board[5])
    print("-----------")
    print(board[6] +" | "+ board[7]+" | "+ board[8])
    print("-----------")
   

#take player input
def playerInput(board):
    inp = int(input("enter a number 1-9:"))
    if  board[inp-1]=="-":
        board[inp-1]= currentplayer
    else:
        print("oops player is already there")

#check for win and tie
def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner = board[0]
        return True 
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True
    

def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner = board[0]
        return True 
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner = board[2]
        return True
   

def checkDiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner = board[0]
        return True 
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner = board[2]
        return True
    


#check win
def checkWin():
    if checkDiag(board):
       printBoard(board)
       print(f"The winner is {winner}")
       gameRunning = False
    elif checkHorizontal(board):
       printBoard(board)
       print(f"The winner is {winner}")
       gameRunning = False
    elif checkrow(board):
       printBoard(board)
       print(f"The winner is {winner}")
       gameRunning = False

#check tie    
def checktie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("its a tie")
        gameRunning = False


#switch the player
def switchplayer():
    global currentplayer
    if  currentplayer == "X":
        currentplayer= "O"
    else :
        currentplayer="X"   

#computer
def computer(board):
 while currentplayer == "O":
     position = random.randint(0, 8)
     if board[position] == "-":
         board[position] = "O"
         break
         switchplayer()


#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checktie(board)
    switchplayer()
    computer(board)
    checkWin()
    checktie(board)        
