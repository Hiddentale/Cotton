from tiles import *
from tile_types import TileTypes
from random import shuffle

# 1: Let a game start where a random cotton board is constructed
# 2: Add the numbers to the tiles


def position_is_in_current_radius(position, current_radius):
    next_radius = current_radius + 1
    return abs(position.get_x()) != next_radius and abs(position.get_y()) != next_radius and abs(position.get_z()) != next_radius

def position_is_not_occupied(position, board):
    return position not in board


def main():
    # For a 4 player, normal game, there are 4 grain tiles, 4 wood tiles, 3 stone tiles, 4 cotton tiles, 3 iron tiles, and 1 desert tile
    # A 5-6 player, normal game, has 5 tiles of each, except for desert, which there are 2 of

    boardgame_tiles = []
    board = []
    amount_of_tiles = {TileTypes.IRON: 3, TileTypes.COTTON: 4, TileTypes.DESERT: 1, TileTypes.GRAIN: 4, TileTypes.OCEAN: 0, TileTypes.STONE: 3, TileTypes.WOOD: 4}  # Make an algorithm out of this

    # don't forget desert does not contain a die number



    for tile, amount in amount_of_tiles.items():
        boardgame_tiles = boardgame_tiles + [tile] * amount

    shuffle(boardgame_tiles)

    center_piece = (0, 0)
    placed_center = False
    current_radius = 1

    # have to remember first tile position of every ring, so we don't place two tiles on same x,y,z coordinates
    new_ring_first_tile = None

    for tile in boardgame_tiles:
        if not placed_center:
            board.append(BoardTile(center_piece, tile))
            placed_center = True
        else:
            if not new_ring_first_tile:
                 new_ring_first_tile = (0, -1 * current_radius)
                 board = board + [BoardTile(new_ring_first_tile, tile)]
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

                print(f"Possible tile placement: {possible_coordinates}")
                      



    print(board)
        
        #boardgame_tiles = boardgame_tiles + [BoardTile(position=(), tile_type=tile)] * amount


    #print(f"All tiles to be used: {boardgame_tiles}\n")

    #indexess = [[0, 3], [3, 7], [7, 12], [12, 16], [16, 19]]
    #boardgame = []
    #def create_row_of_tiles(indexes, boardgame_tiles):
        #row_of_tiles = []
        #for index in range(indexes[0], indexes[1]):
            #row_of_tiles.append(boardgame_tiles[index])
        #return row_of_tiles
    
    #for indexes in indexess:
        #boardgame.append(create_row_of_tiles(indexes, boardgame_tiles))

    #print(f"Boardgame representation: ")
    
    total_number_of_tiles = len(board)
    for row in board:
        #for item in row:
            pass

    #pass


if __name__ == "__main__":
    main()