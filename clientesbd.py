# Ejecutar el programa

import os
import platform

clientes = {}

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("MENU DE OPCIONES")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

limpiar_pantalla()
mostrar_menu()

# A partir de aquí se implementaría la lógica del programa


# Función para añadir un cliente a la base de datos
def agregar_cliente(clientes):
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    preferente = input("¿El cliente es preferencial? (S/N): ")
    preferente = preferente.upper() == "S"
    clientes[dni] = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente": preferente}
    print("Cliente agregado correctamente.\n")

# Función para eliminar un cliente de la base de datos
def eliminar_cliente(clientes):
    dni = input("Ingrese el DNI del cliente a eliminar: ")
    if dni in clientes:
        del clientes[dni]
        print("Cliente eliminado correctamente.\n")
    else:
        print("No se encontró el cliente en la base de datos.\n")

# Función para mostrar los datos de un cliente
def mostrar_cliente(clientes):
    dni = input("Ingrese el DNI del cliente a mostrar: ")
    if dni in clientes:
        cliente = clientes[dni]
        print("Datos del cliente:")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo electrónico: {cliente['correo']}")
        if cliente['preferente']:
            print("Cliente preferencial")
        else:
            print("Cliente no preferencial")
        print()
    else:
        print("No se encontró el cliente en la base de datos.\n")

# Función para listar todos los clientes
def listar_clientes(clientes):
    print("Lista de clientes:")
    for dni, cliente in clientes.items():
        print(f"{dni} - {cliente['nombre']}")
    print()

# Función para listar clientes preferenciales
def listar_clientes_preferenciales(clientes):
    print("Lista de clientes preferenciales:")
    for dni, cliente in clientes.items():
        if cliente['preferente']:
            print(f"{dni} - {cliente['nombre']}")
    print()

# Función principal del programa
def main():
    clientes = {}
    while True:
        print("Menú de opciones:")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferenciales")
        print("6. Terminar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_cliente(clientes)
        elif opcion == "2":
            eliminar_cliente(clientes)
        elif opcion == "3":
            mostrar_cliente(clientes)
        elif opcion == "4":
            listar_clientes(clientes)
        elif opcion == "5":
            listar_clientes_preferenciales(clientes)
        elif opcion == "6":
            print("Programa terminado.")
            break
        else:
            print("Opción inválida.\n")

