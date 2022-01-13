import socket
from network import Network
from _thread import *
from player import Player
from board import Board

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started, listening for connections")

b = Board()


def read_pos(str):  
    return int(str)


def make_str(data):  
    return str(data)


playernumbers = [0, 1]


def threaded_client(conn, player):  
    conn.send(str.encode(make_str(playernumbers[player])))
    # str.encode("Connected"),
    reply = "hello"
    while True:
        try:  
            data = read_pos(conn.recv(2048).decode())
            #    see if client move is valid
            #    valid_move = b.isMoveValid(int(data)-1, currentPlayer)
            #
            #     reply = valid_move
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                print("Sending : ", reply)
                

            conn.sendall(str.encode(make_str(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    # Wait for client connections
    conn, addr = s.accept()
    print("Connected to:", addr)
   # print('currentPlayer', currentPlayer)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

