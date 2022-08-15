"""6. Desarrolla un programa que dada una cierta cantidad de galones, los convierta a litros y dada 
una medida en millas las convierta a metros, ambos con entrada de tipo flotante. """

def main():
    litros = float(input("Ingrese la cantidad de galones: "))
    metros = float(input("Ingrese la cantidad de millas: "))

    litros *= 4.54609
    metros *= 1609.34

    print(f"Usted tiene {round(litros, 2)} litros y {round(metros, 2)} metros")


if __name__ == "__main__":
    main()

