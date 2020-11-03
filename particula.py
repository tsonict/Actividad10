from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0):
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

    @property
    def id(self):
        return self.__id

    @property
    def origenx(self):
        return self.__origenx

    @property
    def origeny(self):
        return self.__origeny

    @property
    def destinox(self):
        return self.__destinox

    @property
    def destinoy(self):
        return self.__destinoy

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia

    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origenx,
            "origen_y": self.__origeny,
            "destino_x": self.__destinox,
            "destino_y": self.__destinoy,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
