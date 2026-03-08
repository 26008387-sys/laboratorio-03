# Ejercicio #3: Clasificación de confort ambiental
def clasificar_ambiente():
    try:
        temperatura = float(input("Ingrese la temperatura (°C): "))
        humedad = float(input("Ingrese la humedad relativa (%): "))
        if temperatura <= 20:
            print("Clasificación: Frío")
        else:
            if humedad < 30:
                print("Clasificación: Seco")
            elif 30 <= humedad <= 60:
                print("Clasificación: Cómodo")
            else: # humedad > 60
                print("Clasificación: Húmedo")     
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")
if __name__ == "__main__":
    clasificar_ambiente()
