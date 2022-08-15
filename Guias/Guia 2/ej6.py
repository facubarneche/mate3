"""6. Un instituto de enseñanza necesita un programa que permita, cada día, procesar observaciones 
sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y 
cada nivel tiene clases en un día de la semana diferente: 
 los lunes se dicta el nivel inicial, 
 los martes el nivel intermedio, 
 los miércoles el nivel avanzado, 
 los jueves son para práctica y 
 los viernes para consultas.
a. Se debe comenzar por solicitar al usuario que ingrese el día (por ejemplo lunes)
b. Una vez indicado el día, el usuario necesita poder indicar si ese día se tomaron 
exámenes, pero sólo si se trata de los niveles inicial, intermedio o avanzado, ya que 
las prácticas y las consultas no tienen exámenes. 
c. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el 
programa le mostrará el porcentaje de aprobados.
d. Si el día fue el correspondiente a práctica, el usuario deberá ingresar el porcentaje 
de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la 
asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
e. Si se trata de las consultas, se deberá emitir "Clase de consulta" y solicitar al 
usuario que ingrese la cantidad de alumnos de la clase y el arancel en $ por cada 
alumno que consulta, para luego imprimir el ingreso total en $"""

def main():

    while True:
        day = input("Ingrese un dia de la semana (lunes, martes, etc...): ").capitalize()

#if day == "Lunes" or day == "Martes" or day == "Miercoles" or day == "Jueves" or day == "Viernes":
        if day in ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes"):
            break
        print("Dia incorrecto")

    if day in ("Lunes", "Martes", "Miercoles"):
        while True:
            exam = input("Hubo examen? (si | no): ").lower()

            if exam == "si":
                exam = True
                break
            elif exam == "no":
                exam = False
                break
            else:
                print("Ingrese si o no")

        if exam:
            passed = int(input("Cuantos alumnos aprobaron?: "))
            no_passed = int(input("Cuantos alumnos desaprobaron?: "))

            success_percent = passed * 100 / (passed + no_passed)

            print(f"El porcentaje de aprobacion es: {round(success_percent, 2)}%")

    if day == "Jueves":
        attendance_percent = round(float(input("Ingrese el porcentaje de asistencia: ")), 2)

        if attendance_percent >= 50:
            print("Asistio la mayoria")
        else:
            print("La mayoria falto")

    if day == "Viernes":
        print("CLASE CONSULTA!!!")
        students = int(input("Ingrese la cantidad de alumnos en la clase: "))
        tax = float(input("Ingrese el arancel: "))

        print(f"El ingreso total es de ${students * tax}")


if __name__ == "__main__":
    main()
