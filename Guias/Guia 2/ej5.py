"""5. Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe 
ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 
400."""

def main():
    year = int(input("Ingrese un año: "))

    if year % 4 == 0:
        if year % 100 != 0:
            print(f"El año ingresado ==> {year}, es bisiestro")
        elif year % 400 == 0:
            print(f"El año ingresado ==> {year}, es bisiestro")
        else:
            print(f"El año ingresado ==> {year}, NO es bisiestro")
    else:
        print(f"El año ingresado ==> {year}, NO es bisiestro")

if __name__ == "__main__":
    main()
