import os
import random

clear=lambda: os.system('cls') #Function that clears the screen
board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] #List with all board fields

def playerInput(): #Function that sets markers for both players
    marker=''
    while not (marker == 'X' or marker == 'O'):
        marker=input("Please choose O or X to start game! ").upper()
        if marker=='O':
            clear()
            print("\nOkay!Now we can start the game,Player1 is 'O' and Player2 is 'X'")
            return ('O','X')
        else:
            clear()
            print("\nOkay!Now we can start the game,Player1 is 'X' and Player2 is 'O'\n")
            return ('X','O')

def displayBoard(board): #Function that display current board status every time something chanegd
    print('\n')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('-------------')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('-------------')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' |')

def changePosition(marker,board,position): #Function that sets marker of player at given position
    if spaceCheck(board,position):
        board[position]=marker
    else:
        askForPosition(marker)

def askForPosition(marker): #Function that calss changePosition() function ,done for aesthetics
    position=int(input('\nPlease choose position(1-9) player '+marker+' '))
    changePosition(marker,board,position)
    clear()

def replay(): #Function that asks players if they wish to play again if no exit program
    print('Game Over')
    choice=input("Do you want to play again? Write 'Y' if you do and 'N' if you don't ").upper()
    if choice=='Y':
        global board
        board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        startGame()
    else:
        exit()

def checkWin(marker): #Function that checks if current status of board is win for one of the players
    return ((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or
            (board[7]==board[8]==board[9]==marker)or(board[1]==board[4]==board[7]==marker)or
                (board[2]==board[5]==board[8]==marker)or(board[3]==board[6]==board[9]==marker)or
                    (board[1]==board[5]==board[9]==marker)or(board[3]==board[5]==board[7]==marker))

def nextTurn(board,marker): #Function that call group of functions that perform 'turn',done for aesthetics
    askForPosition(marker)
    displayBoard(board)

def spaceCheck(board,position): #Function that checks if choosen position is empty
    return board[position]==' '

def fullBoard(board): #Function that checks if board is full => draw
    if ' ' in board:
        return False
    else:
        return True

def startGame(): #Main function
    player1,player2=playerInput()
    displayBoard(board)
    while True:
        nextTurn(board,player1)
        if checkWin(player1): #check fo win
            print('\nPlayer 1 won!')
            break
        elif fullBoard(board): #check for tie
            print("\nIt's a tie!")
            break
        nextTurn(board,player2)
        if checkWin(player2):
            print('\nPlayer 2 won!')
            break
        elif fullBoard(board):
            print("\nIt's a tie!")
            break
    replay()

################################################################################
startGame()

