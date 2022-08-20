"""5. Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista."""

def main():
    array1 = []
    array2 = []

    #Agrega 5 palabras a 2 listas diferentes
    for i in range(5):
        array1.append(input(f"Ingrese la palabra {i + 1} para el primer array: "))
        array2.append(input(f"Ingrese la palabra {i + 1} para el segundo array: "))

    print(list(array1))
    print(list(array2))

    to_delete = input("Ingrese una palabra del primer array que quiera borrar del segundo: ")

    array2.remove(to_delete)

    print(list(array1))
    print(list(array2))


if __name__ == "__main__":
    main()
