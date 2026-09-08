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

    def get_cell(self, row, col):
        return self.grid[row][col]

    def check_neighbor(self, row, col):
        neighbors = []

        if row <0 or row >= self.rows:
            return neighbors

        if col < 0 or col >= self.cols:
            return neighbors

        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                neighbor_row = row + row_offset
                neighbor_col = col + col_offset

                if row_offset != 0 or col_offset != 0:

                    if neighbor_row >= 0 and neighbor_row < self.rows:
                        if neighbor_col >= 0 and neighbor_col < self.cols:
                            neighbors.append(self.grid[neighbor_row][neighbor_col])
        return neighbors


#will be removed once main is created, used to check format and logic of grid is correct
# board = Board()

# for row in board.grid:
#     print(" ".join(row))

#testing check_neighbor 
board = Board()

mid_neighbors = board.check_neighbor(5,5)
print(f"Middle num of neighbors {len(mid_neighbors)}")

corner_neighbors = board.check_neighbor(0,0)
print(f"Corner neighbors {len(corner_neighbors)}")

invalid_neighbors = board.check_neighbor(-1,-1)
print(f"Invalid num of neighbors {len(invalid_neighbors)}")