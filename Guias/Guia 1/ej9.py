"""9. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer 
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso 
pesa 112 g y cada muñeca 75 g. Escribe un programa que lea el número de payasos y muñecas 
vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

def main():
    WEIGHT_CLOWN = 112
    WEIGHT_DOLL = 75

    clowns = int(input("Ingrese el numero de payasos vendidos: "))
    dolls = int(input("Ingrese el numero de muñecas vendidas: "))

    total_weight = clowns * WEIGHT_CLOWN + dolls * WEIGHT_DOLL

    print(f"El peso total enviado en el paquete es de {total_weight}g.")


if __name__ == "__main__":
    main()
