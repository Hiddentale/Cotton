class board_tiles:

    def __init__(self, dimensions):
        self.__dimensions = dimensions
        # list is 3 - 4 - 5 - 4 - 3
        # key: place, value: (number, resource)
        # need algorithm to make a good adjacency list, but position and edges is always the same atleast for original catan without water


class board_tile(board_tiles):

    def __init__(self, position: tuple[int, int], tile_type: int):
        self.__position = position
        self.__tile_type = tile_type

    def get_position(self):
        return self.__position
    
    def get_tile_type(self):
        return self.__tile_type

