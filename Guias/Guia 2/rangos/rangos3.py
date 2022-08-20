#3. Escribe un programa que pida un número entero y emita una lista de números consecutivos del 0 al valor dado.

def main():
    number = int(input("Ingrese un numero entero: "))

    print(list(range(0, number + 1)))


if __name__ == "__main__":
    main()