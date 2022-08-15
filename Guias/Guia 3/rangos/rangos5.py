#5. Escribe un programa que pida dos números enteros y emita la lista de números consecutivos que hay entre ellos, de menor a mayor.

def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))

    if num1 <= num2:
        print(list(range(num1 + 1, num2)))
    else:
        print(list(range(num2 + 1, num1)))   


if __name__ == "__main__":
    main()
