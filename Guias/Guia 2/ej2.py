"""2. Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro 
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día 
ingresado no es ninguno de esos, imprimir otro mensaje."""

def main():

    dia = input("Ingrese un dia de la semana (lunes, martes, etc...): ").lower()

    if dia == "lunes":
        print("Hoy es Lunes =(")
    elif dia == "martes":
        print("Hoy es Martes =S")
    elif dia == "miercoles":
        print("Hoy es miercoles =|")
    elif dia == "jueves":
        print("Hoy es jueves!!!")
    elif dia == "viernes":
        print("Hoy es Vierneeeees =D!!!!")
    elif dia == "sabado":
        print("Hoy es sabadooo!!!")
    elif dia == "domingo":
        print("Hoy es domingo!!!")
    else:
        print("No ingresaste un dia =@")


if __name__ == "__main__":
    main()