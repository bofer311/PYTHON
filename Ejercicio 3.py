# Solicitar la cantidad de toneladas de cada tipo de yerba a comprar
toneladas_tipo_1 = int(input("Ingrese la cantidad de toneladas de yerba tipo 1 que desea comprar: "))
toneladas_tipo_2 = int(input("Ingrese la cantidad de toneladas de yerba tipo 2 que desea comprar: "))

# Preguntar si desea retirar el pedido en el local o necesita flete
flete = input("¿Desea retirar el pedido en el local o necesita flete? (Ingrese '1:Retira' o '2:Flete'): ")

# Solicitar la forma de pago
forma_pago = int(input("Ingrese la forma de pago (1: efectivo, 2: tarjeta de crédito, 3: pagaré): "))

# Calcular el precio total y mostrar el resultado


# Definir la función para calcular el precio total
def precio_total(toneladas_tipo_1, toneladas_tipo_2, flete, forma_pago):
    precio_tipo1 = 36830
    precio_tipo2 = 139954
        
    subtotal_tipo1 = toneladas_tipo_1 * precio_tipo1
    subtotal_tipo2 = toneladas_tipo_2 * precio_tipo2
    subtotal = subtotal_tipo1 + subtotal_tipo2
    
    descuento = 0
    
    if toneladas_tipo_1 + toneladas_tipo_2 > 5:
        descuento = 0.35
    elif toneladas_tipo_1 + toneladas_tipo_2 > 2:
        descuento = 0.2
    elif toneladas_tipo_1 + toneladas_tipo_2 > 1:
        descuento = 0.1
    
    descuento_aplicado = subtotal * descuento
    total_con_descuento = subtotal - descuento_aplicado
    
    if flete == "2":
        flete = (toneladas_tipo_1 + toneladas_tipo_2) * 0.015
        total_con_flete = total_con_descuento * (1 + float(flete))
    else:
        total_con_flete = total_con_descuento

    
    recargo = 0
    
    if forma_pago == 1:
        recargo = -0.05
    elif forma_pago == 2:
        recargo = 0.1
    elif forma_pago == 3:
        recargo = 0.15
    else:
        print("La forma de pago elegida no es válida.")
        print("Las formas de pago admitidas son: 1 (efectivo), 2 (tarjeta de crédito) y 3 (pagaré).")
        return None
    
    recargo_aplicado = total_con_flete * recargo
    total_con_recargo = total_con_flete + recargo_aplicado
    
    print(f"Total de yerba tipo 1: {toneladas_tipo_1}, subtotal: {subtotal_tipo1}")
    print(f"Total de yerba tipo 2: {toneladas_tipo_2}, subtotal: {subtotal_tipo2}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {descuento_aplicado}, ({descuento*100}%)")

