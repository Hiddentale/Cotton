from tile_types import TileTypes
from hexagon import Hexagon

class BoardTile(Hexagon):

    def __init__(self, position: tuple[int, int] = (), tile_type: TileTypes = None, die_number: int = None):
        super().__init__(position[0], position[1])
        self.__tile_type = tile_type
        self.__die_number = die_number

    def __repr__(self) -> str:
        #return f"{self.__tile_type.name} tile"
        #return f"{self.__tile_type.name} tile positioned at ({self.get_x()}, {self.get_y()}, {self.get_z()}) with die number: {self.__die_number}"
        return f"{self.__tile_type.name} tile positioned at ({self.get_x()}, {self.get_y()}, {self.get_z()})"

    def get_position(self):
        return self.__position
    
    def get_tile_type(self):
        return self.__tile_type
    
    def get_die_number(self):
        return self.__die_number


#Need to add coordinates iteratively, starting at center
# Place all tiles, then add ocean tiles which are not part of the original tile set

#unordered_set<Hex> map;
#for (int q = -N; q <= N; q++) {
    #int r1 = max(-N, -q - N);
    #int r2 = min( N, -q + N);
    #for (int r = r1; r <= r2; r++) {
        #map.insert(Hex(q, r, -q-r));
    #}
#}


