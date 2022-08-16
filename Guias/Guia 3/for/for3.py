#3. Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado.

from math import factorial


def main():
    num = int(input("Ingrese un numero N: "))
    factor = 1

    for i in range(1, num + 1):
        factor *= i

    if num > 0:
        print(f"El factorial de {num} es: {factor}")
    else:
        print("El factorial es 0")

if __name__ == "__main__":
    main()
