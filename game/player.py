class Player():
    def __init__(self, name, playernum):
        self.name = name
        self.playernum = playernum

    def getPlayerName(self):
        self.name = input(f"{self.name} please enter your name. Name: ")

    def checkForConnections(self):
        # should check for 2 connections
        # display whether waiting for 2nd player or game can start
        pass
    def updateplayernum(self, num):
        self.playernum = num
    def getplayernum(self):
        return self.playernum


def read_pos(str):  # convert received data (string) to tuple (integer in my case)
    return int(str)


def make_str(data):  # convert tuples to string (before sending data back I think)
    return str(data)


def read_bool(str):
    if str == "True":
        return True
    if str == "False":
        return False
