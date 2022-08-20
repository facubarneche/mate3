"""1. Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar esa cantidad de palabras para crear la lista. Por último, el programa tiene que emitir la lista"""

def main():

    array = []
    num = int(input("Ingrese el numero de palabras de la lista: "))

    for i in range(num):
        array.append(input(f"Ingrese una palabra {i + 1}: "))

    print(list(array))


if __name__ == "__main__":
    main()
