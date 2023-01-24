#display the board
def display_board(board):
  print("\n")
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
  print('\t_____|_____|_____')
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
  print('\t_____|_____|_____')
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
  print("\t     |     |")
  print("\n")

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
  
  '''
  OUTPUT = (PLAYER 1, PLAYER 2)
  
  '''
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input("choose  X or O: ").upper()
  # player1 = marker
  
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')
      
# player1 , player2 = player_input()  

def place_marker(board, marker, position):
  board[position] = marker
  
# place_marker(test_board, '$', 6)

# display_board(test_board)

def win_check(board, mark):
  #win tic tac toe?
  #all rows and check to see if they all share the same marker
  #all columns, check to see if marker matches
  #2 diagonals, check to see match
  
  return ((board[7]==mark and board[8]==mark and board[9]==mark) or  
          (board[4]==mark and board[5]==mark and board[6]==mark) or
          (board[1]==mark and board[2]==mark and board[3]==mark) or
          (board[7]== mark and board[4]==mark and board[1]==mark) or 
          (board[8]== mark and board[5]==mark and board[2]==mark) or 
          (board[9]== mark and board[6]==mark and board[3]==mark) or 
          (board[7]== mark and board[5]==mark and board[3]==mark) or 
          (board[9]== mark and board[5]==mark and board[1]==mark))

# display_board(test_board) 
# win_check(test_board, 'O')

import random

def choose_first():
  flip = random.randint(0,1)
  if flip == 0:
    return 'player 1'
  else:
    return 'player 2'
  
# choose_first() 

def space_check(board, position):
  return board[position] == ' '

def full_board_check(board):
  for i in range(1,10):
    if space_check(board, i):
      return False
  #BOARD IS FULL IF WE RETURN TRUE
  return True

def player_choice(board):
  position = 0
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input('Enter position (1-9): ' ))
    
  return position 

def replay():
  choice = input("Play again? Enter Yes or No: ").upper()
  return choice == 'yes'


#WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')
 
while True:
  
  #PLAY THE GAME
  
  ##SET EVERYTHING UP(BOARD, WHO'S FIRST, CHOOSE MARKERS X, O)
  the_board = [' ']*10
  
  player1, player2 = player_input()
  
  turn = choose_first()
  print(turn + " will go first")
  
  play_game = input("Ready to play? type 'yes' or 'no': ")
  
  if play_game == 'yes':
    game_on = True
  else:
    game_on = False
    
  ##GAME PLAY
  while game_on:
    #player 1 turn
    if turn == 'player 1':
      #show the board
      display_board(the_board)
      #choose position
      position = player_choice(the_board)
      #place the marker on the position
      place_marker(the_board, player1, position)
      
      #check if they won
      if win_check(the_board, player1):
        display_board(the_board)
        print("PLAYER 1 HAS WON, CONGRATULATIONS!!!!!!")
        game_on = False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print("TIE GAME")
          game_on = False
        else:
          turn = 'player 2'
          
    else:
      #show the board
      display_board(the_board)
      #choose position
      position = player_choice(the_board)
      #place the marker on the position
      place_marker(the_board, player2, position)
      
      #check if they won
      if win_check(the_board, player2):
        display_board(the_board)
        print("PLAYER 2 HAS WON, CONGRATULATIONS!!!!!!")
        game_on = False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print("TIE GAME")
          game_on = False
        else:
          turn = 'player 1'
          
      
  if not replay():
    break

#BREAK OUT OF THE WHILE LOOP ON REPLAY()