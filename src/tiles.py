from tile_types import TileTypes

class board_tiles:

    def __init__(self, dimensions: int):
        self.__dimensions = dimensions
        # list is 3 - 4 - 5 - 4 - 3
        # key: place, value: (number, resource)
        
        # need algorithm to make a good adjacency list, but position and edges is always the same atleast for original catan without water
        

    
    def get_dimensions(self):
        return self.__dimensions


class board_tile(board_tiles):

    def __init__(self, position: tuple[int, int] = (), tile_type: TileTypes = None, die_number: int = None):
        self.__position = position
        self.__tile_type = tile_type
        self.__die_number = die_number

    def __repr__(self) -> str:
        return f"{self.__tile_type.name} tile"
        # return f"{self.__tile_type.name} tile positioned at {self.__position} with die number: {self.__die_number}"

    def get_position(self):
        return self.__position
    
    def get_tile_type(self):
        return self.__tile_type
    
    def get_die_number(self):
        return self.__die_number

