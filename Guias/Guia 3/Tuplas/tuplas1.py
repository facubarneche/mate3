#1. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

def main():
    
    tupla = (1, 2, 2, 2, 1, 3, 3, 1, 5, 4, 6, 2, 4)

    num = int(input('Ingrese un numero: '))

    print(f'El numero ingresado se repite {tupla.count(num)} veces')

if __name__ == "__main__":
    main()
