"""3. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera (que debe estar en la lista) por la segunda. Emitir la lista."""

def main():

    array = []

    size = int(input('Ingrese la cantidad de palabras que quiere ingresar en el array: '))

    for i in range(size):
        array.append(input(f"Ingrese la palabra {i + 1}): "))

    word_change1 = input("Ingrese la primera palabra para intercambiar: ")
    word_change2 = input("Ingrese la segunda palabra a intercambiar: ")

    index1 = array.index(word_change1)
    index2 = array.index(word_change2)

    array[index1], array[index2] = array[index2], array[index1]

    print(list(array))



if __name__ == "__main__":
    main()
