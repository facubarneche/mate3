"""
3. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo:

[("Manuel Juarez", 19823451, "Liverpool"),
("Silvana Paredes", 22709128, "Buenos Aires"),
("Rosa Ortiz", 15123978, "Glasgow"),
("Luciana Hernandez", 38981374, "Lisboa")]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:

[("Buenos Aires", "Argentina"),
("Glasgow", "Escocia"),
("Lisboa", "Portugal"),
("Londres", "Inglaterra"),
("Madrid", "España")]

Hacer un programa que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, emitir a qué ciudad y país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa.
"""


def main():
    leave = False
    personal_info = ([], [])

    while leave is False:

        name = input('Ingrese el nombre: ')
        dni = int(input('Ingrese el DNI: '))
        destination = input(f'Ingrese el destino de {name}: ')
        personal_info[0].append( (name, dni, destination) )
        city = input('Ingrese la cuidad: ')
        country = input('Ingrese el pais: ')
        personal_info[1].append( (city, country))

        quest = input('Si se agregaron todas las personas presione "S", \
de lo contrario presione enter: ').upper()

        if quest == 'S':
            leave = True

    ask_dni = int(input('Busque la cuidad y pais que viaja un pasajero con su dni: '))
    ask_country = input('Ingrese un pais para saber cuantos pasajeros viajan hacia ese destino: ')

    count = 0

    for tupla in personal_info[0]:
        if ask_dni in tupla:
            index = personal_info[0].index(tupla)
            print(f'Cuidad: {personal_info[1][index][0]}, Pais: {personal_info[1][index][1]}')

        if ask_country in tupla:
            count += 1

    print(f'El destino {ask_country} va a ser visitado por {count} persona/s')

if __name__ == "__main__":
    main()
