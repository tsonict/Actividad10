from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = 0, origen_x = 0-500, origen_y = 0-500, destino_x = 0-500, destino_y = 0-500, velocidad = 0, red = 0-255, green = 0-255, blue = 0-255):
        self.__id = id
        self.__origenx = origen_x
        self.__origeny = origen_y
        self.__destinox = destino_x
        self.__destinoy = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return (
            'ID: ' + str(self.__id) + '\n' +
            'Origen x: ' + str(self.__origenx) + '\n' +
            'Origen y: ' + str(self.__origeny) + '\n' +
            'Destino x: ' + str(self.__destinox) + '\n' +
            'Destino y: ' + str(self.__destinoy) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n'
        )
