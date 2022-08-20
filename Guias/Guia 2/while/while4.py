#4. Escribe un programa que pida números enteros mientras el usuario ingresa números cada vez más grandes, el programa emite en cada iteración el número anterior ingresado y finaliza ingresando un número menor.

def main():
    num = int(input("Ingrese un numero: "))
    new_num = int(input("Ingrese un numero: "))

    while num < new_num:
        print(f"Numero anterior --> {num}")
        num = new_num
        new_num = int(input("Ingrese un numero: "))

    print(f'Se finalizo el programa ya que {num} es mayor a {new_num}')


if __name__ == "__main__":
    main()
