import sys

from DictIndex import DictIndex
from Square import Square

if __name__ == '__main__':
    name = sys.argv[1]
    file = open(name, 'r')
    lines = file.readlines()
    grid = [[Square.from_string(square) for square in line.split(",")]for line in lines ]

    dictionary = DictIndex.from_dict_file("words.txt")

    SIZE = len(grid[0])
    grid.insert(0, [None for sq in grid[0]])
    grid.append([None for sq in grid[0]])
    for grid_line in grid:
        grid_line.append(None)
        grid_line.insert(0, None)

    squares = set()

    for row_idx in range(1, 1 + SIZE):
        for col_idx in range(1, 1+SIZE):
            for row_shift in [1,0,-1]:
                square = grid[row_idx][col_idx]
                squares.add(square)
                for col_shift in [1,0,-1]:
                    if row_shift != 0 or col_shift != 0:
                        square.add_neighbor(grid[row_idx+row_shift][col_idx+col_shift])

    for square in squares:
        print("==============")
        if square.starts > 0:
            dict_prefix = dictionary.prefix(square.letter)
            for word in square.search(dict_prefix, set()):
                if len(word) >= 4:
                    print(word)
