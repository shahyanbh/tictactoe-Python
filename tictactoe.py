#this is the code for making tic tac toe on Python
#initial write date 16-Dec-2020
#play tic tac toe on console
player = "X"
Decision = False
bot = 'Y'
import random
from math import inf as infinity

#filling boards wikth blank dashes
board = ["-" for board in range(9)]
def StartGreet():
    print("Hello, welcome lets play TIC TAC TOE!")
    print("you can play this by selecting grid number from 1-9")
    print("Below shoes the numbering scheme of the grid:")
    print("1 | 2 | 3 \n4 | 5 | 6 \n7 | 8 | 9 ")
    print("Lets start :) May the best tic tacker wins")

def DisplayBoard(boardin):
    #displaying initia; board
    for board_peice in range(0,8,3):
        print(boardin[board_peice] + " | " + boardin[board_peice + 1] +" | "+ boardin[board_peice +2]) 
 
    
def take_input():
    location = input("Enter a number from 1-9: ")
    positions = ['1','2','3','4', '5', '6', '7', '8', '9' ]
    valid = False
    #check if the nuber is in the range and a person is not duplicating a move
    while not valid:
        while location not in positions:
            print("invaid input")
            location = input("Enter a number from 1-9: ")
        if board[int(location)-1] == '-':
            valid = True
        else:
            print("you can't go there..")
            location = input("Enter a number from 1-9: ")



#print(location)
    location = int(location)
    board[location-1] = player


def turn():
    print(player + "'s turn")
    if bot == 'Y':
        if player == 'X':
            take_input()
        else:
            if player == 'O':
              #Dumb_bot()
              AI(board)
    else:
        take_input()


def finddepth(boardState):
    depth = 0
    for i in range(len(boardState)):
        if board[i] == '-':
            depth += 1
    return depth        

def Minimax(currentBoard, depth, maximizingPlayer, player):
    #defining base case
    if maximizingPlayer:
        player = 'O'
    else:
        player = 'X'

    Result = checkWin(currentBoard, player)

    if depth == 0 and Result:
        if maximizingPlayer:
            return 10 #resturn a socre of one as its the bottom of board we win
        else:
            return -10 #return a score of a negative one as its a loss

    if depth== 0 and not Result:
        return 0 #for draw
    
    if Result:
        if maximizingPlayer:
            return 10 * depth #the value of win by levels
        else:
            return -10 * depth  #the value of loss by levels      

    if maximizingPlayer:
        MaxEval = -infinity
        for spot in range(len(currentBoard)):
            if currentBoard[spot] == '-':
                currentBoard[spot] = 'O'
                eval = Minimax(currentBoard, depth -1 , False, 'X')
                MaxEval = max(MaxEval, eval)
                currentBoard[spot] = '-'
        return MaxEval
    else:
        MinEval = infinity
        for spot in range(len(currentBoard)):
            if currentBoard[spot] == '-':
                currentBoard[spot] = 'X'
                eval = Minimax(currentBoard, depth -1 , True, 'O')
                MinEval = min(MinEval, eval)
                currentBoard[spot] = '-'
        return MinEval


def AI(board):
    previousEval = 0
    bestmove = 2

    #to find the spcaes left in the board 
    #for the sample it should output 2
    spacesLeft = board.count('-')
    #find the space and put a move and run mininmax on it
    for spot in range(len(board)):
        if board[spot] == '-':
            board[spot] = 'O'
            eval = Minimax(board, spacesLeft-1, False, player)
            if eval >= previousEval:
                previousEval = eval
                bestmove = spot
            board[spot] = '-'
    
    board[bestmove] = 'O'





def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player ="X"        

def Dumb_bot():
    move = random.randrange(1,9)
    while board[move-1] != "-":
        move = random.randrange(1,9)
    board[move-1] = player

   


def checkWin(positions, player):
    #checking horizontal result
    for i in range(0,8,3):
        if positions[i] == positions[i +1 ] == positions[i + 2] == player:
            return True
    #checking vertical result
    for i in range(3):            
        if positions[i] == positions[i +3 ] == positions[i + 6] == player:
            return True
    #checking diagnol result
    if positions[0] == positions[4] == positions[8] == player:
            
            return True
    if positions[2] == positions[4] == positions[6] == player:
            
            return True
    
    
    return False

    
def AskForPlayer():
    global bot
    bot= input("Do you want to play single player: Y/N:  ")
    bot = bot.upper()
    while (bot != "Y") and (bot!= "N"):
        print('invalid input')
        bot= input("Do you want to play single player: Y/N:  ")
        bot = bot.upper()
    print(bot)

#main program flow
StartGreet()    
DisplayBoard(board)
AskForPlayer()

for count_turn in range(9):
    turn()
    DisplayBoard(board)
    Decision = checkWin(board, player)
    if Decision == True:
        print(player + " wins")
        break
    switch_player()
    if count_turn == 8:
        print("DRAW!!")






