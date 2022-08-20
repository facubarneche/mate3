"""6. Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (crear una lista distinta)."""

def main():
    array = []
    reverse_array = []

    for i in range(5):
        array.append(input(f"Ingrese la palabra {i + 1}: "))

    reverse_array = array.copy()
    reverse_array.reverse()

    print(list(array))
    print(list(reverse_array))

if __name__ == "__main__":
    main()
