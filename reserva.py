from excepciones import ErrorDatosReserva, ErrorEstadoReserva


class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if not self.cliente or not self.servicio:
                raise ErrorDatosReserva("Datos incompletos para la reserva")

            self.estado = "Confirmada"
            print(f"✅ Reserva confirmada para {self.cliente.get_nombre()}")

        except Exception as e:
            print("❌ Error:", e)
            self.guardar_log(e)

        finally:
            print("🔄 Proceso de confirmación finalizado\n")

    def cancelar(self):
        try:
            if self.estado != "Confirmada":
                raise ErrorEstadoReserva("No se puede cancelar una reserva no confirmada")

            self.estado = "Cancelada"
            print("⚠️ Reserva cancelada")

        except Exception as e:
            print("❌ Error:", e)
            self.guardar_log(e)

        finally:
            print("🔄 Proceso de cancelación finalizado\n")

    def guardar_log(self, error):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"ERROR: {str(error)}\n")
