from particula import Particula
import json
class Particulas:
    def __init__(self):
        self.__list_particulas = []

    def agregar_final(self, particula:Particula):
        self.__list_particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__list_particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__list_particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__list_particulas
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__list_particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__list_particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0



#p01 = Particula(id=123, origen_x= 20, origen_y= 25, destino_x= 70, destino_y= 30, velocidad= 14123, red= 10, green= 255, blue= 255)
#p02 = Particula(id=222, origen_x= 34, origen_y= 21, destino_x= 100, destino_y= 7, velocidad= 23984, red= 60, green= 0, blue= 0)


#particulas = Particulas()

#particulas.agregar_final(p01)
#particulas.agregar_inicio(p02)
#particulas.mostrar()