import math

def Opciones():
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponente")
    print("6. Cuadrado")

def Calculadora():
    opcion = input("Elige una opción: ")

    if opcion == "6":
        num = float(input("Ingresa el número: "))
        
        if num < 0:
            print("Error: no se permiten números negativos")
        else:
            resultado = math.pow(num, 2)
            print("Resultado:", resultado)

    else:
        num1 = float(input("Ingresa la primera cantidad: "))
        num2 = float(input("Ingresa la segunda cantidad: "))

        if num1 < 0 or num2 < 0:
            print("Error: no se permiten números negativos")
            return

        if opcion == "1":
            resultado = math.fsum([num1, num2])

        elif opcion == "2":
            resultado = math.fsum([num1, -num2])

        elif opcion == "3":
            resultado = math.prod([num1, num2])

        elif opcion == "4":
            if num2 == 0:
                print("Error: no se puede dividir entre 0")
                return
            resultado = math.prod([num1, 1/num2])

        elif opcion == "5":
            resultado = math.pow(num1, num2)

        else:
            print("Opción no válida")
            return

        print("Resultado:", resultado)

Opciones()
Calculadora()