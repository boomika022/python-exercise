


































#-----global variabels-----
board=['-','-','-',
       '-','-','-',
       '-','-','-']
#if game is still going
game_still_going = True

#anyone won or tie?
winner = None

#whos turn is this
current_player = "x" 
players = None 

def display_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def handel_turn(players):
    
    position=int(input('enter your position from 1-9: '))
    position=position-1

    board[position]="x"

handel_turn(players)
    
display_board()

def play_game():

    #display a initial board 
    display_board()
handel_turn(current_player)

    
    #while the game is still going   
while game_still_going:
          if winner=='x' or winner=='o':
              print(winner+'won')

def game_over():
     check_for_win
     #check rows
     #check colunms
     #check diagonals
     check_if_tie
     return

def check_for_win():

     
    
    return
def check_if_tie():
     return

def flip_players():
     return
    
    




#board
#display board
#play game
#handel turn    
#check win
 #check rows
 #check columns
 #check diagonals
#check tie
#flip players
#game_over
