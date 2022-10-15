"""
1.Escribe un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.
"""

import pandas as pd
import numpy as np

def main():

    #Setea el formato de float a 2 decimales
    pd.options.display.float_format = '${:,.2f}'.format

    #Forma un rango desde el ingreso hasta el egreso por ej: (2002, 2020) 2019 + 1
    years_range = range(int(input('Ingrese desde que año: ')), int(input('Hasta que año: ')) + 1)
    
    #Crea una lista de numeros randoms de low a high, con un tamaño igual al rango anterior
    data = np.random.uniform(low=0, high=99999.99, size=(len(years_range)))

   # id = pd.date_range(start=datetime.date(years_range[0],1,1), periods=len(years_range), freq='AS')
    
    #Transformo el array de randoms en una serie
    serie = pd.Series(data, index=years_range)
    print(f'\nPandas serie sin descuento: \n{serie}')

    #Le resto el 10% de descuento
    serieDescuento = serie - serie * 0.1

    print(f'\nPandas serie con descuento: \n{serieDescuento}')

if __name__ == '__main__':
    main()
