import sqlite3

# Función para crear la tabla de personas en la base de datos
def crear_tabla_personas():
    conn = sqlite3.connect('personas.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS personas
                      (nombre TEXT, apellido TEXT, dni TEXT, telefono TEXT, email TEXT, direccion TEXT)''')

    conn.commit()
    conn.close()

# Función para agregar una persona a la base de datos
def agregar_persona():
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    dni = input('Ingrese el DNI: ')
    telefono = input('Ingrese el teléfono: ')
    email = input('Ingrese el email: ')
    direccion = input('Ingrese la dirección: ')

    conn = sqlite3.connect('personas.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO personas VALUES (?, ?, ?, ?, ?, ?)", (nombre, apellido, dni, telefono, email, direccion))

    conn.commit()
    conn.close()

    print('La persona ha sido agregada correctamente.')

# Función para mostrar las personas registradas en la base de datos
def mostrar_personas():
    conn = sqlite3.connect('personas.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()

    if len(personas) == 0:
        print('No se han registrado personas.')
    else:
        for persona in personas:
            print('Nombre:', persona[0])
            print('Apellido:', persona[1])
            print('DNI:', persona[2])
            print('Teléfono:', persona[3])
            print('Email:', persona[4])
            print('Dirección:', persona[5])
            print('---')

    conn.close()

# Función principal que controla el menú
def menu():
    crear_tabla_personas()

    while True:
        print('1. Agregar persona')
        print('2. Mostrar personas registradas')
        print('3. Salir')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            agregar_persona()
        elif opcion == '2':
            mostrar_personas()
        elif opcion == '3':
            break
        else:
            print('Opción inválida. Intente nuevamente.')

menu()




