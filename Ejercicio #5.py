# Ejercicio #5: Leap Year Checker (Año Bisiesto)
def check_leap_year():
    try:
        # 1. Solicitar el año al usuario (en inglés)
        year = int(input("Please enter year: "))
        if year <= 0:
            print("Invalid year")
        else:
            # 2. Aplicar las reglas para año bisiesto
            # Regla 1: Múltiplo de 400
            # Regla 2: Múltiplo de 4 Y NO de 100
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")               
    except ValueError:
        # En caso de que el usuario no ingrese un número entero
        print("Invalid input. Please enter a numeric year.")

if __name__ == "__main__":
    check_leap_year()
