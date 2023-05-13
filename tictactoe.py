def printBoard():
    for row in range(len(board)):
        print("--   --  --")
        for col in range(len(board[row])):
            if col % 2 == 1:
                print(f" {board[row][col]}", end="")
            else:
                print(f"| {board[row][col]} |", end="")
        print()

def checkBoard(r,c):
    char=board[r][c]
    win=False
    i=0
    while i<len(board):
        if board[r][i]==char:
            win=True
            i+=1
        else:
            win=False
            break
    if win:
        return win
    j=0
    while j<len(board):      
        if board[j][c]==char:
            win=True
            j+=1  
        else:
            win=False
            break
    if win:
        return win
    k=0
    while k<len(board):
        if board[k][k]==char:
            win=True
            k+=1 
        else:
            win=False
            break
    if win:
        return win
    l=0
    while l<len(board):
        if board[l][2-l]==char:
            win=True
            l+=1
        else:
            win=False
            break
    if win:
        return win
    else:
        return win
                
def placeCharacter(pos,char,count):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==int(pos):
                board[row][col]=char
                return checkBoard(row,col)
      
def gameInitialization():
    global player1,player2
    player1 = input("Enter player 1's name:")
    player2 = input("Enter player 2's name:")
    print(f"{player1}, your character is X")
    print(f"{player2}, your character is O")
    
def runGame():
    counter = 0
    f=False
    p_name=None
    while counter<9:
        printBoard()
        if counter%2==0:
            if (placeCharacter(input(f"{player1}, where do you want to place 'X':"),'X',counter)):
                p_name = player1
                f = True
                break
        else:
            if (placeCharacter(input(f"{player2}, where do you want to place 'O':"),'O',counter)):
                p_name = player2
                f = True
                break
        counter+=1
    printBoard()
    if f == False:
        print("The game ends in a draw.")
    else:
        print(f"{p_name} has won the game!!!!")

board = [[1,2,3],[4,5,6],[7,8,9]]
player1 = player2 = None
gameInitialization()
runGame()
