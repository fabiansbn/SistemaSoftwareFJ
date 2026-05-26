from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva


# LISTAS
clientes = []
servicios = []
reservas = []


# FUNCIÓN LOGS
def guardar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(mensaje + "\n")


# MENÚ
while True:

    print("\n===== SOFTWARE FJ =====")
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    try:

        # REGISTRAR CLIENTE
        if opcion == "1":

            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")

            cliente = Cliente(
                nombre,
                correo,
                telefono
            )

            clientes.append(cliente)

            guardar_log("Cliente registrado")

            print("Cliente registrado correctamente")

        # CREAR SERVICIO
        elif opcion == "2":

            print("\n1. Reserva Sala")
            print("2. Alquiler Equipo")
            print("3. Asesoría")

            tipo = input("Seleccione servicio: ")

            nombre = input("Nombre del servicio: ")
            precio = float(input("Precio base: "))

            if tipo == "1":

                horas = int(input("Horas: "))

                servicio = ReservaSala(
                    nombre,
                    precio,
                    horas
                )

            elif tipo == "2":

                dias = int(input("Días: "))

                servicio = AlquilerEquipo(
                    nombre,
                    precio,
                    dias
                )

            elif tipo == "3":

                horas = int(input("Horas: "))

                servicio = AsesoriaEspecializada(
                    nombre,
                    precio,
                    horas
                )

            else:
                raise ValueError("Tipo de servicio inválido")

            servicios.append(servicio)

            guardar_log("Servicio creado")

            print("Servicio creado correctamente")

        # CREAR RESERVA
        elif opcion == "3":

            if len(clientes) == 0:
                raise ValueError("No hay clientes registrados")

            if len(servicios) == 0:
                raise ValueError("No hay servicios registrados")

            cliente = clientes[0]
            servicio = servicios[0]

            duracion = int(input("Duración: "))

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            reserva.confirmar_reserva()

            reservas.append(reserva)

            guardar_log("Reserva realizada")

            print("Reserva creada correctamente")

        # VER RESERVAS
        elif opcion == "4":

            if len(reservas) == 0:
                print("No hay reservas")

            else:

                for reserva in reservas:

                    print()
                    print(reserva.mostrar_reserva())

        # SALIR
        elif opcion == "5":

            guardar_log("Programa finalizado")

            print("Saliendo del sistema...")

            break

        else:
            print("Opción inválida")

    except Exception as e:

        guardar_log(f"ERROR: {e}")

        print("Error:", e)

    finally:

        guardar_log("Operación ejecutada")