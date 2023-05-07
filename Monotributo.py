categorias = {
    1: {"limite_ingresos": 999657.23, "monto_mensual": 5750.25},
    2: {"limite_ingresos": 1485976.96, "monto_mensual": 6430.38},
    3: {"limite_ingresos": 2080367.73, "monto_mensual": 7351.10},

}

ingresos_brutos = float(input("Ingrese sus ingresos brutos mensuales promedio menor a $173.000: "))
if ingresos_brutos > 173000:
    print("Lo siento, su ingreso supera el límite permitido para el régimen del monotributo. Por favor consulte otro sistema este es obsoleto")
else:
    tipo_actividad = int(input("Ingrese el tipo de actividad (1 para Venta, 2 para Servicios): "))
    ingresos_anuales = ingresos_brutos * 12

categoria = 1
while categoria < 1 and ingresos_anuales > categorias[categoria]["limite_ingresos"]:
    categoria += 1


monto_mensual = categorias[categoria]["monto_mensual"]
print(f"Su categoría es la {categoria} y debe abonar ${monto_mensual:.2f} mensuales en concepto de monotributo.")


# opcion = 0

# while opcion != 1 and opcion != 2:
#     opcion = int(input("Seleccione una opción (1 o 2): "))

#     if opcion == 1:
#         print("Usted esta en Locacion de servicio .")
#     elif opcion == 2:
#         print("Usted esta en Ventas .")
#     else:
#         print("Opción inválida. Intente de nuevo.")

        