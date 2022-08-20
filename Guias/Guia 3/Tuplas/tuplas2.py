#2. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla.

def main():

    tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    index = int(input('Ingrese un indice: '))

    print(tupla[index])

if __name__ == "__main__":
    main()
