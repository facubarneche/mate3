#4. Muestre los N primeros números de la secuencia de Fibonacci, siendo n un dato entero.

def main():
    num = int(input("Ingrese un numero N: "))
    a, b = 0, 1

    for i in range(num + 1):
        print(f"{a}, ")
        a, b = b, a + b



if __name__ == "__main__":
    main()
