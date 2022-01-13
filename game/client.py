from player import Player
from board import Board
from network import Network


def read_bool(str):
    if str == "True":
        return True
    if str == "False":
        return False

def read_pos(str):  
    return int(str)


def make_str(data):  
    return str(data)


def startNewGame():
    valid_session = True
    player2 = False
    n = Network()  # connect to server
    b = Board()
    currentPlayer = read_pos(n.get_id())
    print('currentPlayer:', currentPlayer)
    players = [Player("Player 1"), Player("Player 2")]
    players[currentPlayer].getPlayerName()
    players[currentPlayer].updateplayernum(currentPlayer)
    print('Waiting for 2nd player to join')
    while not player2:
        currentPlayer = read_pos(n.get_id())
        if currentPlayer == 1:
            print('Player 2 connected')
            players[currentPlayer].getPlayerName()
            players[currentPlayer].updateplayernum(currentPlayer)
            player2 = True

    while valid_session:
        b.draw_board()

        valid_move = False
        win = False
        win_check = n.send()
        if b.isWin(currentPlayer) or b.isHorizontalWin(currentPlayer):  # pass moves to server and call
            print(f"{players[currentPlayer].name} wins!")
            break
            # Send move to server; end game if player won or a player disconnected
        if b.moves_played > 54:
            print(f"Tie! Game over")
            break
        # GET current player
        if currentPlayer == 1:
            currentPlayer = 0
        else:
            currentPlayer = 1

        while not valid_move:
            user_move = input(f"It's {players[currentPlayer].name}'s turn - please enter column (1-9) ")
            #   valid_move = read_bool(n.send(make_str(user_move)))) #send server user move

            win_check = read_bool(n.send(make_str(user_move)))
           
            if win_check:
                print(f"{players[currentPlayer].name} wins!")
                break
            ##  valid_move = b.isMoveValid(int(user_move)-1, currentPlayer) #replace with server reply after line 34 line 34
            if valid_move:
                continue
            else:
                print("Move invalid, please choose another column")


startNewGame()
