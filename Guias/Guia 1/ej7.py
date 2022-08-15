"""7. Realiza un programa que dadas una cantidad de segundos los conveirta en horas, minutos y 
segundos.
"""

def main():
    hora, minutos, segundos = 0, 0, 0

    while True:
        usuario = int(input("Ingrese una cantidad de segundos: "))
        user = usuario

        while usuario != 0:
            if usuario >= 3600:
                hora += 1
                usuario -= 3600
            elif usuario >= 60:
                minutos += 1
                usuario -= 60
            else:
                segundos = usuario
                usuario = 0

        print(f"{user} ==> {hora}:{minutos}:{segundos}")

        repeticion = int(input("Ingrese 1 para repetir: "))

        if repeticion != 1:
            break

if __name__ == "__main__":
    main()
