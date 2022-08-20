#5. Escribe un programa que pida números mientras no se escriba un número negativo. El programa terminará emitiendo la suma de los números ingresados.


def main():
    total_plus = 0
    num = int(input('Ingrese un numero: '))

    while num >= 0:
        total_plus += num
        num = int(input('Ingrese un numero: '))

    print(f'La suma total de los numeros pares ingresados es {total_plus}')

if __name__ == '__main__':
    main()
