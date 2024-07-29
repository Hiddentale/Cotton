from tiles import *
from tile_types import TileTypes

# 1: Let a game start where a random cotton board is constructed
# 2: Add the numbers to the tiles


def main():
    # For a 4 player, normal game, there are 4 grain tiles, 4 wood tiles, 3 stone tiles, 4 cotton tiles, 3 iron tiles, and 1 desert tile
    # A 5-6 player, normal game, has 5 tiles of each, except for desert, which there are 2 of
    boardgame_tiles = []
    amount_of_tiles = {TileTypes.IRON: 3, TileTypes.COTTON: 4, TileTypes.DESERT: 1, TileTypes.GRAIN: 4, TileTypes.OCEAN: 0, TileTypes.STONE: 3, TileTypes.WOOD: 4}

    for tile, amount in amount_of_tiles.items():
        boardgame_tiles = boardgame_tiles + [board_tile(position=(), tile_type=tile)] * amount

    print(boardgame_tiles)
    pass


if __name__ == "__main__":
    main()