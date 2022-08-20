#7. Escribe un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos. El programa terminará cuando se escriba un número que no esté comprendido entre los dos valores iniciales y emitirá la cantidad de números ingresados.

def main():
    count = 0
    min_num = int(input('Ingrese un numero minimo: '))
    max_num = int(input('Ingrese un numero maximo: '))

    num = int(input('Ingrese un numero situado entre ellos: '))

    while min_num <= num <= max_num:
        count += 1
        num = int(input('Ingrese un numero situado entre ellos: '))

    print(f'Usted ha ingresado {count} numeros entre el minimo y el maximo')

if __name__ == '__main__':
    main()
