from abc import ABC, abstractmethod


# CLASE ABSTRACTA
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def mostrar_servicio(self):
        pass


# SERVICIO 1
class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):

        return self.precio_base * self.horas

    def mostrar_servicio(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Horas: {self.horas}\n"
            f"Costo: {self.calcular_costo()}"
        )


# SERVICIO 2
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):

        super().__init__(nombre, precio_base)

        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")

        self.dias = dias

    def calcular_costo(self):

        return self.precio_base * self.dias

    def mostrar_servicio(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Días: {self.dias}\n"
            f"Costo: {self.calcular_costo()}"
        )


# SERVICIO 3
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):

        return (self.precio_base * self.horas) + 50000

    def mostrar_servicio(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Horas: {self.horas}\n"
            f"Costo: {self.calcular_costo()}"
        )