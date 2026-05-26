class Cliente:

    def __init__(self, nombre, correo, telefono):

        # VALIDAR NOMBRE
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # VALIDAR CORREO
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido")

        # VALIDAR TELÉFONO
        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números")

        # ENCAPSULACIÓN
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # SETTERS
    def set_nombre(self, nuevo_nombre):

        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        self.__nombre = nuevo_nombre

    def set_correo(self, nuevo_correo):

        if "@" not in nuevo_correo or "." not in nuevo_correo:
            raise ValueError("Correo inválido")

        self.__correo = nuevo_correo

    def set_telefono(self, nuevo_telefono):

        if not nuevo_telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números")

        self.__telefono = nuevo_telefono

    # MOSTRAR INFORMACIÓN
    def mostrar_info(self):

        return (
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )