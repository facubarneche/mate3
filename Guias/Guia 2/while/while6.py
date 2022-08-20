#6. Escribe un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números introducidos supere el límite inicial.

def main():
    total_plus = 0
    limit = int(input('Ingrese un valor limite positivo: '))

    while total_plus <= limit:
        total_plus += int(input('Ingrese un numero: '))


if __name__ == '__main__':
    main()
