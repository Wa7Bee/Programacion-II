import math

class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distancia(self, puntoRandom, y=None):

        if isinstance(puntoRandom, MiPunto):
            x2 = puntoRandom.getX()
            y2 = puntoRandom.getY()

        else:
            x2 = puntoRandom
            y2 = y

        return math.sqrt(
            (x2 - self.__x) ** 2 +
            (y2 - self.__y) ** 2
        )

punto1 = MiPunto()
punto2 = MiPunto(10, 30.5)
distancia = punto1.distancia(punto2)

print(distancia)