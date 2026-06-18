from servicio import Servicio
from excepciones import DatosInvalidosError as DatosInvalidos, ServicioNoDisponibleError as ServicioNoDisponible

# SERVICIO 1 - RESERVA DE SALAS

class ReservaSala(Servicio):

    def __init__(self, nombre, costo_por_hora, horas, disponible=False, aire_acondicionado=False, internet=False, videobeam=False):
        super().__init__(nombre)

        if horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        self.costo_por_hora = costo_por_hora
        self.horas = horas
        self.disponible = disponible
        self.aire_acondicionado = aire_acondicionado
        self.internet = internet
        self.videobeam = videobeam

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponible(
                "Sala no disponible"
            )

    def calcular_costo(self, descuento=0):

        costo = self.costo_por_hora * self.horas

        total = costo - descuento

        if total < 0:
            raise DatosInvalidos(
                "El descuento no puede ser mayor al costo"
            )

        return total

    def descripcion(self):
        return (
            f"Servicio: {self._nombre} | "
            f"Horas: {self.horas} | "
            f"Características: disponible={self.disponible}, aire_acondicionado={self.aire_acondicionado}, "
            f"internet={self.internet}, videobeam={self.videobeam}"
        )

# SERVICIO 2 - ALQUILER DE EQUIPOS

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_por_dia, tipo, dias):
        super().__init__(nombre)

        if dias <= 0:
            raise DatosInvalidos(
                "Los días deben ser mayores a 0"
            )

        self.costo_por_dia = costo_por_dia
        self.tipo = tipo
        self.dias = dias

    def validar_disponibilidad(self, cantidad):
        # Sin límite en la cantidad de días
        pass

    def calcular_costo(self, impuesto=0):

        costo_base = self.costo_por_dia * self.dias

        # Aumento del 10% en el precio final
        costo_con_aumento = costo_base * 1.10

        total = costo_con_aumento + impuesto

        return total

    def descripcion(self):
        return (
            f"Servicio: {self._nombre} | "
            f"Tipo: {self.tipo} | "
            f"Días: {self.dias}"
        )

# SERVICIO 3 - ASESORIAS ESPECIALIZADAS

class Asesoria(Servicio):

    def __init__(self, nombre, costo_por_hora, especialidad, experto_certificado=False):
        super().__init__(nombre)

        self.costo_por_hora = costo_por_hora
        self.especialidad = especialidad
        self.experto_certificado = experto_certificado

    def validar_disponibilidad(self):
        if not self.experto_certificado:
            raise ServicioNoDisponible(
                "Asesor no certificado"
            )

    def calcular_costo(self, horas, descuento=0, impuesto=0):

        if horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        subtotal = self.costo_por_hora * horas

        total = subtotal - descuento + impuesto

        if total < 0:
            raise DatosInvalidos(
                "El total no puede ser negativo"
            )

        return total

    def descripcion(self):
        return (
            f"Servicio: {self._nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Experto certificado: {self.experto_certificado}"
        )

# SERVICIO 4 - SERVICIOS COMPLEMENTARIOS

class ServicioComplementario(Servicio):

    servicios_disponibles = [
        "parqueadero",
        "zona de registro",
        "soporte tecnico"
    ]

    def __init__(self, servicio, cantidad_horas):
        super().__init__("Servicio Complementario")

        if servicio.lower() not in self.servicios_disponibles:
            raise ServicioNoDisponible(
                "Servicio complementario no disponible"
            )

        if cantidad_horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        self.servicio = servicio.lower()
        self.cantidad_horas = cantidad_horas

    def calcular_costo(self):

        costos = {
            "parqueadero": 7500,
            "zona de registro": 15000,
            "soporte tecnico": 40000
        }

        return costos[self.servicio] * self.cantidad_horas

    def descripcion(self):
        return (
            f"Servicio: {self.servicio} | "
            f"Horas: {self.cantidad_horas}")
