# 1. Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
# No considerar el caso en que ambos números son iguales.

def main():

    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))

    if num1 < num2:
        print(f"{num1} es menor que {num2}")
    elif num1 > num2:
        print(f"{num1} es mayor que {num2}")
    else:
        print("Ambos numeros son iguales")

if __name__ == "__main__":
    main()
