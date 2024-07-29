class Hexagon:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__z = (-1 * x) - y

        assert self.__x + self.__y + self.__z == 0

    def __eq__(self, hexagon):
        return hexagon.get_q() == self.__x and hexagon.get_r() == self.__y
    
    def __add__(self, hexagon):
        return Hexagon(self.__x + hexagon.get_x(), self.__y + hexagon.get_y())
    
    def __sub__(self, hexagon):
        return Hexagon(self.__x - hexagon.get_x(), self.__y - hexagon.get_y())
    
    def __mult__(self, hexagon):
        return Hexagon(self.__x * hexagon.get_x(), self.__y * hexagon.get_y())
    
    def __div__(self, hexagon):
        return Hexagon(self.__x // hexagon.get_x(), self.__y // hexagon.get_y())
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    pass