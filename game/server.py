import socket
from client import Player
from board import Board
from network import Network

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started, listening for connections")

players = [Player("Player 1"), Player("Player 2")]

def startNewGame():
    valid_session = True
    b = Board()
    currentPlayer = 0
    players[currentPlayer].getPlayerName()
    players[currentPlayer + 1].getPlayerName()

    while valid_session:
        b.draw_board()
          
        valid_move = False
        if b.isWin(currentPlayer) or b.isHorizontalWin(currentPlayer):
            print(f"{players[currentPlayer].name} wins!")
            break
                
        if b.moves_played > 54:
            print(f"Tie! Game over")
            break
        if currentPlayer == 1:
            currentPlayer = 0
        else:
            currentPlayer = 1
            
        while not valid_move:
            user_move = input(f"It's {players[currentPlayer].name}'s turn - please enter column (1-9)")
            valid_move = b.isMoveValid(int(user_move)-1, currentPlayer)
            if valid_move:
                continue 
            else:
                print("Move invalid, please choose another column")

startNewGame()