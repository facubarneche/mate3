"""10. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al 
año. Estos ahorros no se cobran hasta finales de año y se te suman al balance final de tu 
cuenta de ahorros. Escribe un programa que comience leyendo la cantidad de dinero depositada 
en la cuenta de ahorros. El programa debe calcular y mostrar por pantalla la cantidad de 
ahorros tras el primer, segundo y tercer año. Redondea cada cantidad a dos decimales."""

def main():
    INTEREST = 4.0

    deposit = float(input("Ingrese el monto depositado: "))

    for i in range(3):
        deposit += (deposit * INTEREST) / 100

    print(f"El ahorro obtenido es ${round(deposit, 2)}")

if __name__ == "__main__":
    main()
