"""
3. Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
"""

def main():
    students = {}

    count = int(input('Ingrese la cantidad de alumnos: '))

    for _ in range(count):
        grades = []
        flag = True

        while flag:
            flag = False
            new_student = input('Ingrese el nombre del nuevo alumno: ').capitalize()

            for student in students:
                if student == new_student:
                    print('Alumno existente!')
                    flag = True

        while True:
            new_grade = int(input(f'Ingrese la nota de {new_student}: '))

            #Para cuando es negativo, o mayor a 10 ya que no existe cierta nota
            if new_grade < 0 or new_grade > 10:
                break

            grades.append(new_grade)

        students[new_student] = grades

    for student, grades in students.items():
        average = 0
        for grade in grades:
            average += grade
        average /= len(grades)

        print(f'El promedio de {student} es {round(average, 2)}')



if __name__ == '__main__':
    main()
