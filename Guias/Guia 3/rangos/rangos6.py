#6. Escribe un programa que pida dos números enteros par2 emita la lista de números pares que hapar2 entre ellos (incluidos ellos mismos si son pares)

def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))

    def pairs(par1, par2):
        if par1 % 2 == 0 and num2 % 2 == 0:
            print(list(range(par1, par2 + 1, 2)))
        elif par1 % 2 == 0:
            print(list(range(par1, par2, 2)))
        elif par2 % 2 == 0:
            print(list(range(par1 + 1, par2 + 1, 2)))
        else:
            print(list(range(par1 + 1, par2, 2)))

    if num1 <= num2:
        pairs(num1, num2)
    else:
        pairs(num2, num1)

if __name__ == "__main__":
    main()
