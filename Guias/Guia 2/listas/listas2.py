"""2. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas 
veces aparece esa palabra en la lista."""

def main():

    array = []
    cont = 0
    num = int(input("Ingrese el numero de palabras del array: "))

    for i in range(num):
        array.append(input(f"Ingrese la palabra {i + 1}: "))

    find_word = input("Ingrese una palabra a buscar: ")

    for i in range(num):
        if array[i] == find_word:
            cont += 1

    print(f"La palabra buscada '{find_word}', se encontró un total de {cont} veces")

if __name__ == "__main__":
    main()
