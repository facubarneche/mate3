#2. Escribe un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa termina y emitirá los números.

def main():
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: "))

    while num1 >= num2:
        num2 = int(input("El ultimo numero debe ser mayor al primero: "))

    print(f"Los numeros son {num1} y {num2}")

if __name__ == "__main__":
    main()
