from tiles import *
from tile_types import TileTypes
from random import shuffle

# 1: Let a game start where a random cotton board is constructed
# 2: Add the numbers to the tiles


def main():
    # For a 4 player, normal game, there are 4 grain tiles, 4 wood tiles, 3 stone tiles, 4 cotton tiles, 3 iron tiles, and 1 desert tile
    # A 5-6 player, normal game, has 5 tiles of each, except for desert, which there are 2 of
    # Represent the board as a hexagonal grid by letting half the rows being even numbers and the other rows odd numbers, distance between adjacent tiles will then be 1
    boardgame_tiles = []
    boardgame = []
    amount_of_tiles = {TileTypes.IRON: 3, TileTypes.COTTON: 4, TileTypes.DESERT: 1, TileTypes.GRAIN: 4, TileTypes.OCEAN: 0, TileTypes.STONE: 3, TileTypes.WOOD: 4}

    for tile, amount in amount_of_tiles.items():
        boardgame_tiles = boardgame_tiles + [BoardTile(position=(), tile_type=tile)] * amount

    shuffle(boardgame_tiles)

    print(f"All tiles to be used: {boardgame_tiles}\n")

    indexess = [[0, 3], [3, 7], [7, 12], [12, 16], [16, 19]]
    boardgame = []
    def create_row_of_tiles(indexes, boardgame_tiles):
        row_of_tiles = []
        for index in range(indexes[0], indexes[1]):
            row_of_tiles.append(boardgame_tiles[index])
        return row_of_tiles
    
    for indexes in indexess:
        boardgame.append(create_row_of_tiles(indexes, boardgame_tiles))

    print(f"Boardgame representation: ")
    for row in boardgame:
        print(row)

    pass


if __name__ == "__main__":
    main()