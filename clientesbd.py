clientes = {}

def mostrar_menu():
    print("MENU DE OPCIONES")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

def agregar_cliente():
    # Pedir los datos del cliente
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    preferente = input("¿El cliente es preferencial? (S/N): ")
    preferente = preferente.upper() == "S"
    
    # Crear un diccionario con los datos del cliente y agregarlo a la base de datos
    clientes[dni] = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    
    print("Cliente agregado correctamente.\n")

def eliminar_cliente():
    # Pedir el DNI del cliente a eliminar
    dni = input("Ingrese el DNI del cliente a eliminar: ")
    
    if dni in clientes:
        # Eliminar al cliente de la base de datos si existe
        del clientes[dni]
        print("Cliente eliminado correctamente.\n")
    else:
        print("No se encontró el cliente en la base de datos.\n")

def mostrar_cliente():
    # Pedir el DNI del cliente a mostrar
    dni = input("Ingrese el DNI del cliente a mostrar: ")
    
    if dni in clientes:
        # Obtener los datos del cliente y mostrarlos
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

def listar_clientes():
    print("Lista de clientes:")
    
    for dni, cliente in clientes.items():
        # Mostrar el DNI y nombre de cada cliente
        print(f"{dni} - {cliente['nombre']}")
    
    print()

def listar_clientes_preferentes():
    print("Lista de clientes preferenciales:")
    
    for dni, cliente in clientes.items():
        # Mostrar el DNI y nombre de los clientes preferenciales
        if cliente['preferente']:
            print(f"{dni} - {cliente['nombre']}")
    
    print()

# Mostrar el menú inicial
mostrar_menu()

while True:
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        eliminar_cliente()
    elif opcion == "3":
        mostrar_cliente()
    elif opcion == "4":
        listar_clientes()
    elif opcion == "5":
        listar_clientes_preferentes()
    elif opcion == "6":
        print("Programa terminado.")
        break
    else:
        print("Opción inválida.\n")
