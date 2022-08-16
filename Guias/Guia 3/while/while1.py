"""1. Escribe un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación pida números hasta que se hayan ingresado la cantidad de números indicada."""

def main():
    num = abs(int(input("Ingrese la cantidad de numeros que quiere ingresar: ")))
    i = 0

    while i < num:
        input(f"Ingrese el numero #{i + 1}: ")
        i += 1

if __name__ == "__main__":
    main()
