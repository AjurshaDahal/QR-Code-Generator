def playerInput(board):
    inp = int(input("enter a number 1-9:"))
    if inp >=1 and inp <=9 and board[inp-1]=="-":
        board[inp-1]=currentplayer
    else:
        print("oops player is already there")