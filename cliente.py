# Sistema Software FJ
# Clase cliente con POO, encapsulacion y manejo de excepciones

import re
import logging

# Configuracion de logs
logging.basicConfig(
    filename='errores.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ==========================
# Excepciones personalizadas
# ==========================

class ClienteError(Exception):
    """Excepcion base para errores de Cliente"""
    pass

class NombreInvalidoError(ClienteError):
    pass

class CorreoInvalidoError(ClienteError):
    pass

class CelularInvalidoError(ClienteError):
    pass

# ==========================
# Clase Cliente
# ==========================

class Cliente:

    def __init__(self, nombre, correo, celular):
        try:
            self.__nombre = None
            self.__correo = None
            self.__celular = None

            self.set_nombre(nombre)
            self.set_correo(correo)
            self.set_celular(celular)

        except Exception as e:
            logging.error(f"Error al crear cliente: {e}")
            raise

    # ==========================
    # Métodos SET (Encapsulación)
    # ==========================
    
    def set_nombre(self, nombre):
        try:
            if not nombre or not nombre.strip():
                raise NombreInvalidoError("El nombre no puede estar vacio")
            self.__nombre = nombre.strip()
        except NombreInvalidoError as e:
            logging.error(e)
            raise

    def set_correo(self, correo):
        try:
            patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(patron, correo):
                raise CorreoInvalidoError("Correo electronico invalido")
            self.__correo = correo
        except CorreoInvalidoError as e:
            logging.error(e)
            raise

    def set_celular(self, celular):
        try:
            if not celular.isdigit() or len(celular) < 10:
                raise CelularInvalidoError("Numero de celular invalido")
            self.__celular = celular
        except CelularInvalidoError as e:
            logging.error(e)
            raise

    # ==========================
    # Métodos GET
    # ==========================  

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_celular(self):    
        return self.__celular

    # ==========================
    # Método mostrar información
    # ==========================

    def mostrar_informacion(self):
        try:
            print("--- Informacion del Cliente ---")
            print(f"Nombre: {self.__nombre}")
            print(f"Correo: {self.__correo}")
            print(f"Celular: {self.__celular}")
        except Exception as e:
            logging.error(f"Error al mostrar informacion: {e}")

# ==========================
# Ejemplo de uso
# ==========================
 
if __name__ == "__main__":
    try:
        cliente1 = Cliente("Juan Perez", "juan@email.com", "3001234567")
        cliente1.mostrar_informacion()

        print("\nIntentando crear cliente inválido...")
        cliente2 = Cliente("", "correo_invalido", "123")

    except ClienteError as ce:
        print(f"Error de cliente: {ce}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Programa finalizado.")
                                  

