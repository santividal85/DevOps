def separador():
    print("-" * 40)

def obtener_dato(campo, tipo=str, opciones=None):
    while True:
        valor = input("  " + campo + ": ").strip()
        if not valor:
            print("  Advertencia: El campo no puede estar vacio. Intenta de nuevo.")
            continue
        try:
            valor = tipo(valor)
        except ValueError:
            print("  Advertencia: Valor invalido. Ingresa un numero valido.")
            continue
        if opciones and valor.lower() not in opciones:
            print("  Opciones validas: " + ", ".join(opciones))
            continue
        return valor

def main():
    print()
    separador()
    print("   REGISTRO DE DATOS PERSONALES")
    separador()
    print("  Llena los campos a continuacion:\n")

    nombre   = obtener_dato("Nombre completo")
    edad     = obtener_dato("Edad", tipo=int)
    sexo     = obtener_dato("Sexo (masculino/femenino/otro)", opciones=["masculino", "femenino", "otro"])
    estatura = obtener_dato("Estatura en cm (ej. 175)", tipo=float)

    print()
    separador()
    print("   DATOS REGISTRADOS")
    separador()
    print("  Nombre:   " + nombre)
    print("  Edad:     " + str(edad) + " años")
    print("  Sexo:     " + sexo.capitalize())
    print("  Estatura: " + str(estatura) + " cm")
    separador()
    print()

if __name__ == "__main__":
    main()
