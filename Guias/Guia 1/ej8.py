"""8. Escribe un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
índice de masa corporal, lo almacene en una variable, y muestre por pantalla redondeado con 
dos decimales.
"""

def main():
    peso = float(input("Ingrese su peso en Kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))

    masa = peso / (estatura **2)    #Peso / la estatura al cuadrado = IMC

    print(f"Su Indice de masa corporal es: {round(masa, 2)}")

if __name__ == "__main__":
    main()
