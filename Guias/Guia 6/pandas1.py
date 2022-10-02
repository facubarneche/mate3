"""
1.Escribe un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.
"""

import pandas as pd

def main():

    years = int(input('Ingrese la cantidad de años: '))
    info = []

    for i in range(years):
        new_data = int(input(f'Ingrese el valor {i + 1}: '))
        info.append(new_data) 

    s = pd.Series(info)
    print(s)

if __name__ == '__main__':
    main()
