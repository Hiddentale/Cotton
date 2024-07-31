from tile_types import TileTypes

def get_amount_of_tiles(number_of_players):
    if number_of_players < 5:
        return {TileTypes.IRON: 3, TileTypes.COTTON: 4, TileTypes.DESERT: 1, TileTypes.GRAIN: 4, TileTypes.OCEAN: 0, TileTypes.STONE: 3, TileTypes.WOOD: 4}
    elif number_of_players < 7:
        return {TileTypes.IRON: 5, TileTypes.COTTON: 6, TileTypes.DESERT: 2, TileTypes.GRAIN: 6, TileTypes.OCEAN: 0, TileTypes.STONE: 5, TileTypes.WOOD: 6}
    else:
        raise Exception("7+ player games have not been implemented yet!")