#2. Escribe un programa que le permita realizar la suma de los primeros N números impares.

from re import I


def main():
    num = int(input("Ingrese un numero N: "))
    impares = 0

    for i in range(num):
        if(i % 2 == 1):
            impares+= i

    print(f"La suma de los numeros impares hasta el numero {num} elegido (excluyendo este ultimo), es: {impares}")


if __name__ == "__main__":
    main()
