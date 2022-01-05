class Board():
    def __init__(self):
        self.board = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.recent_move = 0
        self.moves_played = 0

    def draw_board(self):
        count = 0
        for key in self.board:
            
            if key == -1:
                print(' [ ] ', end="")

            if key == 0:
                print(' [X] ', end="")
                
            if key == 1:
                print(' [O] ', end="")
            count = count + 1
            
            if (count % 9)  == 0:
                print("\n")
        for col in range(9):
            print(f" ({col+1}) ", end="")
     
    def place_disk(self, move, playerNum):
            self.board[move] = playerNum
            self.recent_move = move
            self.moves_played = self.moves_played + 1
    
    def isMoveValid(self, move, playerNum):
        bottom_col = {8:1, 7:2, 6:3, 5:4, 4:5, 3:6, 2:7, 1:8, 0:9} #col selected:val to subtract from highest board index
        final_spot = 54 #index of col 9 row 6
        numToSubtract = bottom_col[move]
        desired_move = final_spot - numToSubtract

        if type(move) is str:
            return False

        if move not in range(9):
            return False
        
        for num in range(6):
            if self.board[desired_move] == -1:
                self.place_disk(desired_move, playerNum)
                return True
            else:
                desired_move = desired_move - 9
        return False

    def findHorizontalWins(self, smallest, playerNum):
        winning_combo = []
        for num in range(3):
            smallest = smallest + 1
            if self.board[smallest] == playerNum:
                winning_combo.append(smallest)
        if len(winning_combo) == 3:
            return True
        else:
            return False
        
    def isWinner(self, playerNum):
        index_dirs = [1, 8, 9, 10]
        for idx in index_dirs:
            furthest = idx * 4
    
            if idx == 1:
            #check for potential horizontal wins separately to prevent false positives;
            #refactor
                if self.recent_move in range(9):
                    if (self.recent_move + furthest) in range(9) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(9) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                if self.recent_move in range(9, 18):
                    if (self.recent_move + furthest) in range(9, 18) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move 
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(9, 18) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    
                if self.recent_move in range(18, 27):
                    if (self.recent_move + furthest) in range(18, 27) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(18, 27) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    
                if self.recent_move in range(27, 36):
                    if (self.recent_move + furthest) in range(27, 36) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(27, 36) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    
                if self.recent_move in range(36, 45):
                    if (self.recent_move + furthest) in range(36, 45) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(36, 45) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                  
                if self.recent_move in range(45, 54):
                    if (self.recent_move + furthest) in range(45, 54) and self.board[self.recent_move + furthest] == playerNum:
                        smallest = self.recent_move
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                    if (self.recent_move - furthest) in range(45, 54) and self.board[self.recent_move - furthest] == playerNum:
                        smallest = furthest
                        win = self.findHorizontalWins(smallest, playerNum)
                        return win
                else:
                    return False
                    
            
                
            if self.recent_move + furthest in range(54) and self.board[self.recent_move + furthest] == playerNum:
                smallest = self.recent_move
                
                winning_combo = []
                winning_combo.append(smallest)
                winning_combo.append(furthest)
                incremented_idx = smallest + idx
                for num in range(3): 
                    
                    if self.board[incremented_idx] == playerNum:
                        winning_combo.append(incremented_idx)
                    incremented_idx = incremented_idx + idx

                if len(winning_combo) == 5:
                    return True 
                
            if self.recent_move - furthest in range(54) and self.board[self.recent_move - furthest] == playerNum:
                smallest = furthest
                winning_combo = []
                winning_combo.append(smallest)
                winning_combo.append(self.recent_move)
                
                incremented_idx = smallest + idx
                for num in range(3): 
                    
                    
                    if self.board[incremented_idx] == playerNum:
                        winning_combo.append(incremented_idx)
                    incremented_idx = incremented_idx + idx
                if len(winning_combo) == 5:
                    return True
                
        return False