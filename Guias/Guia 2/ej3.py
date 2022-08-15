"""3. Crear un programa que permita al usuario elegir un candidato por el cual votar. Las 
posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el 
mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el 
usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
indicar “Opción errónea”.
"""

def main():

    candidato = input("Ingrese el candito a votar (A, B, C): ").lower()

    print(candidato)
    if candidato == "a":
        print("Usted voto por el partido rojo")
    elif candidato == "b":
        print("Usted voto por el partido verde")
    elif candidato == "c":
        print("Usted voto por el partido azul")
    else:
        print("No existe ese partido")


if __name__ == "__main__":
    main()