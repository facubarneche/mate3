#3. Escribe un programa que pida números decimales mientras el usuario escriba número mayores que el primero.


def main():
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: "))

    while num1 < num2:
        num2 = int(input("El ultimo numero no debe ser mayor al primero: "))

    print(f"Los numeros son {num1} y {num2}")

if __name__ == "__main__":
    main()
