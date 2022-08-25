"""
2. Crear un programa donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

def main():

    fruits = {
        'banana': 90,
        'manzana': 135,
        'kiwi': 246,
        'anana': 180,
        'frutillas': 150,
        'pera': 100,
        'melon': 130
    }

    while True:

        flag = False
        fruit_name = input('Ingrese el nombre de una fruta: ').lower()

        for fruit, price in fruits.items():
            if fruit_name == fruit:
                amount = int(input('Ingrese la cantidad de kilos que se vendieron: '))
                final_price = amount * price
                flag = True
                print(f'{amount} kilo/s de {fruit} sale un total de ${final_price}')

        if flag is False:
            print('Error, fruta inexistente')

        repeat = input('Para finalizar presione "S", para continuar "enter": ').upper()

        if repeat == 'S':
            break



if __name__ == '__main__':
    main()
