from tiles import *
from tile_types import TileTypes
from random import shuffle
from amount_of_tiles import get_amount_of_tiles

# 1: Let a game start where a random cotton board is constructed
# 2: Add the numbers to the tiles
# 3: Draw the center hexagon to the window
# 4: Draw the rest of the hexagons iteratively
# 4: Add players
# 5: Add player hands

def position_is_in_current_radius(position, current_radius):
    next_radius = current_radius + 1
    return abs(position.get_x()) != next_radius and abs(position.get_y()) != next_radius and abs(position.get_z()) != next_radius

def position_is_not_occupied(position, board):
    return position not in board

def place_boardgame_tiles_hexagonally(boardgame_tiles, board):
    center_piece = (0, 0)
    placed_center = False
    current_radius = 1
    new_ring_first_tile = None

    for tile in boardgame_tiles:
        if not placed_center:
            board.append(BoardTile(center_piece, tile))
            placed_center = True
        else:
            if not new_ring_first_tile:
                 new_ring_first_tile = (0, -1 * current_radius)
                 board.append(BoardTile(new_ring_first_tile, tile))
            else:
                current_tile_neighbours = board[-1].find_neighbours()
                possible_coordinates = []

                for position in current_tile_neighbours:
                    if position_is_not_occupied(position, board) and position_is_in_current_radius(position, current_radius):
                        possible_coordinates.append(position)

                if not possible_coordinates:
                    current_radius += 1
                    new_ring_first_tile = None
                else:
                    new_position = possible_coordinates[0].get_position()
                    board.append(BoardTile(new_position, tile))
    return board
    

def main():

    boardgame_tiles = []
    board = []
    number_of_players = 5
    amount_of_tiles = get_amount_of_tiles(number_of_players) # There is a problem here, original catan only has a center for the 2-4 player games, but wouldn't it be more balanced to keep the center in 5+ player games?

    for tile, amount in amount_of_tiles.items():
        boardgame_tiles = boardgame_tiles + [tile] * amount

    shuffle(boardgame_tiles)

    board = place_boardgame_tiles_hexagonally(boardgame_tiles, board)
    return board

    #print(board)


if __name__ == "__main__":
    main()