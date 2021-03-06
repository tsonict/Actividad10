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

    def orden_id(self):
        return self.__list_particulas.sort(key=lambda particula: particula.id)

    def orden_distancia(self):
        return self.__list_particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    def orden_velocidad(self):
        return self.__list_particulas.sort(key=lambda particula: particula.velocidad)


    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__list_particulas
        )

    def __len__(self):
        return len(self.__list_particulas)


    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__list_particulas):
            particula = self.__list_particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

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