class Board:
    rows = 10
    cols = 10

    def __init__(self):
        self.grid= []

        for row in range(self.rows):
            new_row = []
            for column in range(self.cols):
                new_row.append("*") #using "*" as placeholder till further along in program
                                    #used to make sure set up of board is correct
            self.grid.append(new_row)



#will be removed once main is created, used to check format and logic of grid is correct
board = Board()

for row in board.grid:
    print(" ".join(row))
