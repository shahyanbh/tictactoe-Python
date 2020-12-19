#this is the code for making tic tac toe on Python
#initial write date 16-Dec-2020
#play tic tac toe on console
player = "X"
Decision = False
bot = 'Y'
import random

#filling boards wikth blank dashes
board = ["-" for board in range(9)]
def StartGreet():
    print("Hello, welcome lets play TIC TAC TOE!")
    print("you can play this by selecting grid number from 1-9")
    print("Below shoes the numbering scheme of the grid:")
    print("1 | 2 | 3 \n4 | 5 | 6 \n7 | 8 | 9 ")
    print("Lets start :) May the best tic tacker wins")

def DisplayBoard():
    #displaying initia; board
    for board_peice in range(0,8,3):
        print(board[board_peice] + " | " + board[board_peice + 1] +" | "+ board[board_peice +2]) 
 
    
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



    print(location)
    location = int(location)
    board[location-1] = player


def turn():
    print(player + "'s turn")
    if bot == 'Y':
        if player == 'X':
            take_input()
        else:
            if player == 'O':
              Dumb_bot()
    else:
        take_input()

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





def checkWin():
    #checking horizontal result
    for i in range(0,8,3):
        if board[i] == board[i +1 ] == board[i + 2] == player:
            return True
    #checking vertical result
    for i in range(3):            
        if board[i] == board[i +3 ] == board[i + 6] == player:
            return True
    #checking diagnol result
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6] == player:
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
DisplayBoard()
AskForPlayer()

for count_turn in range(9):
    turn()
    DisplayBoard()
    Decision = checkWin()
    if Decision == True:
        print(player + " wins")
        break
    switch_player()
    if count_turn == 8:
        print("DRAW!!")






