"""4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje 
“es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de 
más de un carácter, informarle que no se puede procesar el dato."""

def main():

    while True:
        letra = input("Ingrese una letra: ").lower()

        if letra >= 'a' <= 'z' and len(letra) == 1:
            break
        print("El dato no se puede procesar")

    print(letra)

if __name__ == "__main__":
    main()
