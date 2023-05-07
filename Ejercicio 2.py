
# Definimos las categorías del monotributo y sus límites de ingresos
categorias = {
    1: {"limite_ingresos": 208739.25, "monto_mensual": 2840.00},
    2: {"limite_ingresos": 313108.88, "monto_mensual": 3717.50},
    3: {"limite_ingresos": 417478.50, "monto_mensual": 4248.50},
    4: {"limite_ingresos": 626217.75, "monto_mensual": 5359.50},
    5: {"limite_ingresos": 834957.00, "monto_mensual": 7312.50},
    6: {"limite_ingresos": 1043696.25, "monto_mensual": 9015.00},
    7: {"limite_ingresos": 1252435.50, "monto_mensual": 10517.50},
    8: {"limite_ingresos": 1565544.25, "monto_mensual": 12222.50},
    9: {"limite_ingresos": 1878653.00, "monto_mensual": 14027.50}
}

# Pedimos al usuario que ingrese sus ingresos brutos mensuales promedio y el tipo de actividad
ingresos_brutos = float(input("Ingrese sus ingresos brutos mensuales promedio: "))
tipo_actividad = int(input("Ingrese el tipo de actividad (1 para Venta, 2 para Servicios): "))

# Calculamos los ingresos anuales promedio
ingresos_anuales = ingresos_brutos * 12

# Buscamos la categoría correspondiente según los ingresos anuales
categoria = 1
while categoria < 10 and ingresos_anuales > categorias[categoria]["limite_ingresos"]:
    categoria += 1

# Mostramos la categoría y el monto mensual correspondiente
monto_mensual = categorias[categoria]["monto_mensual"]
print(f"Su categoría es la {categoria} y debe abonar ${monto_mensual:.2f} mensuales en concepto de monotributo.")

