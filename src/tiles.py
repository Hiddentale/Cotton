from tile_types import TileTypes
from hexagon import Hexagon

class BoardTile(Hexagon):

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

