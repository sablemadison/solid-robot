class Board():
    def __init__(self):
        self.board = [-1 for _ in range(54)]
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

    def isHorizontalWin(self, playerNum):
        if self.recent_move < 9:
            min = 0
            max = 8
        if self.recent_move < 18:
            min = 9
            max = 17
        if self.recent_move < 27:
            min = 18
            max = 26
        if self.recent_move < 45:
            min = 36
            max = 44
        else:
            min = 44
            max = 53
        if self.recent_move + 4 in range(min, max) and self.board[self.recent_move + 4] == playerNum:
            starting_idx = self.recent_move + 4
            winning_row = []
            for i in range(4):
                starting_idx = starting_idx - 1
                if self.board[starting_idx] == playerNum:
                    winning_row.append(self.board[starting_idx])
            if len(winning_row) > 3:
                return True
        if self.recent_move - 4 in range(min, max) and self.board[self.recent_move - 4] == playerNum:
            starting_idx = self.recent_move -4
            winning_row = []
            for i in range(4):
                starting_idx = starting_idx + 1
                if self.board[starting_idx] == playerNum:
                    winning_row.append(self.board[starting_idx])
            if len(winning_row) > 3:
                return True
        
        else:
            return False
        
    def isWin(self, playerNum):
        index_dirs = [8, 9, 10]
        for idx in index_dirs:
            print('index:', idx)
            furthest = idx * 4
            print('furthest:', furthest)
            winning_row = []   
            if self.recent_move + furthest in range(54) and self.board[self.recent_move + furthest] == playerNum:
                smallest = self.recent_move
                
                winning_row.append(smallest)
                winning_row.append(furthest)
                incremented_idx = smallest + idx
                for num in range(3): 
                    
                    if self.board[incremented_idx] == playerNum:
                        winning_row.append(incremented_idx)
                    incremented_idx = incremented_idx + idx

                if len(winning_row) >= 5:
                    return True 
                
            if self.recent_move - furthest in range(54) and self.board[self.recent_move - furthest] == playerNum:
                smallest = furthest
                winning_row.append(smallest)
                winning_row.append(self.recent_move)
                
                incremented_idx = smallest + idx
                for num in range(3): 
                    
                    if self.board[incremented_idx] == playerNum:
                        winning_row.append(incremented_idx)
                    incremented_idx = incremented_idx + idx
                if len(winning_row) >= 5:
                    return True
                
        return False