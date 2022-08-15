#4. Escribe un programa que pida dos números enteros (el segundo mayor que el primero) y emita listas de números consecutivos al derecho y al revés.

def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero mayor al primero: "))

    print(list(range(num1, num2 + 1)), list(range(num2, num1 - 1, -1)))

if __name__ == "__main__":
    main()
