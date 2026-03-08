# Ejercicio #4: Sistema de suscripciones Claro Video

def calcular_suscripcion():
    print("--- Sistema de Facturación Claro Video ---")

    # 1. Leer la cuota normal mensual del paquete HD
    cuota_hd = float(input("Ingrese el precio mensual del paquete HD: "))

    # 2. Elegir el tipo de paquete
    tipo_paquete = input("Ingrese el tipo de paquete ('HD' o '4K'): ").upper()

    # Determinar el costo base mensual según la calidad
    if tipo_paquete == "4K":
        costo_base = cuota_hd * 3
    else:
        costo_base = cuota_hd
    meses = int(input("Ingrese la cantidad de meses a contratar (1, 2, 4 o 12): "))
    # 3. Determinar el descuento según los meses
    if meses == 1:
        descuento = 0.0
    elif meses == 2:
        descuento = 0.10  # 10%
    elif meses == 4:
        descuento = 0.20  # 20%
    elif meses == 12:
        descuento = 0.35  # 35%
    else:
        print("Opción de meses no válida.")
        return

    # 5. Calcular el total con descuento aplicado
    # Fórmula: (Costo Mensual * Meses) - Descuento
    precio_sin_descuento = costo_base * meses
    total_pagar = precio_sin_descuento * (1 - descuento)

    # 6. Desplegar resultados
    print("\n--- Resumen de Compra ---")
    print(f"Paquete seleccionado: {tipo_paquete}")
    print(f"Meses contratados: {meses}")
    print(f"Costo mensual base: ${costo_base:.2f}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total a pagar por la suscripción: ${total_pagar:.2f}")


if __name__ == "__main__":
    calcular_suscripcion()
