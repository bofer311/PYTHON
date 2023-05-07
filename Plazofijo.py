def plazo_fijo(capital, interes_anual, meses, renovacion_anual, inflacion_mensual):
    # Convertir el interés anual a mensual y calcular el interés mensual
    interes_mensual = (interes_anual / 12) / 100

    # Calcular el capital final con interés simple
    capital_simple = capital * (1 + interes_mensual * meses)

    # Calcular el capital final con interés compuesto
    capital_compuesto = capital * (1 + interes_mensual) ** meses

    # Calcular el capital final con renovación anual y compuesto
    capital_renovado = capital_compuesto
    if renovacion_anual:
        for i in range(meses):
            if i % 12 == 0:
                capital_renovado *= (1 + interes_mensual) ** 12

    # Calcular el capital final con inflación
    capital_inflacion = capital
    for i in range(meses):
        capital_inflacion *= (1 - inflacion_mensual)
    
    # Mostrar los resultados
    print(f"Capital invertido: ${capital:.2f}")
    print(f"Interés mensual: {interes_mensual * 100:.2f}%")
    print(f"Capital final con interés simple: ${capital_simple:.2f}")
    print(f"Capital final con interés compuesto: ${capital_compuesto:.2f}")
    print(f"Capital final con renovación anual: ${capital_renovado:.2f}")
    print(f"Capital final con inflación: ${capital_inflacion:.2f}")

# Ejemplo de uso:
capital = float(input("Ingrese el capital a invertir: "))
interes_anual = 9.1
meses = int(input("Ingrese el número de meses a invertir: "))
renovacion_anual = input("¿Desea renovación anual? (S/N): ").lower() == "s"
inflacion_mensual = 0.06 / 12

plazo_fijo(capital, interes_anual, meses, renovacion_anual, inflacion_mensual)
