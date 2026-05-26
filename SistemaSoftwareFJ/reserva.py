# Gestión de reservas

from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # CONFIRMAR RESERVA
    def confirmar_reserva(self):

        if self.estado == "Confirmada":
            raise ReservaError("La reserva ya está confirmada")

        self.estado = "Confirmada"

    # CANCELAR RESERVA
    def cancelar_reserva(self):

        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya está cancelada")

        self.estado = "Cancelada"

    # MOSTRAR INFORMACIÓN
    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo Total: {self.servicio.calcular_costo()}"
        )
