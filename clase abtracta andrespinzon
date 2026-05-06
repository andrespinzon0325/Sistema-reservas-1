from abc import ABC, abstractmethod

# Clase abstracta
class Servicio(ABC):
    
    def __init__(self, nombre):
        self._nombre = nombre  # encapsulación

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Clase derivada 1
class ReservaSala(Servicio):
    
    def __init__(self, nombre, horas, costo_por_hora):
        super().__init__(nombre)
        self.horas = horas
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self):
        return self.horas * self.costo_por_hora

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# Clase derivada 2
class AlquilerEquipo(Servicio):
    
    def __init__(self, nombre, dias, costo_por_dia):
        super().__init__(nombre)
        self.dias = dias
        self.costo_por_dia = costo_por_dia

    def calcular_costo(self):
        return self.dias * self.costo_por_dia

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


# Clase derivada 3
class Asesoria(Servicio):
    
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_costo(self):
        return self.horas * self.tarifa

    def descripcion(self):
        return f"Asesoría especializada de {self.horas} horas"


# Ejemplo de polimorfismo
servicios = [
    ReservaSala("Sala VIP", 3, 50),
    AlquilerEquipo("Proyector", 2, 30),
    Asesoria("Consultoría IT", 5, 100)
]

for servicio in servicios:
    print(servicio.descripcion())
    print("Costo:", servicio.calcular_costo())
    print("------")
