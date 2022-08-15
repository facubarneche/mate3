"""4. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista."""

def main():

    array = []

    size = int(input("Ingrese el cantidad de palabras a agregar: "))

    for i in range(size):
        array.append(input(f"Ingrese la palabra {i + 1}) "))

    word_delete = input("Ingrese una palabra ha eliminar: ")

    array.remove(word_delete)

    print(list(array))

if __name__ == "__main__":
    main()
