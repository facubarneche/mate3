"""
4. El archivo autos.xlsx contiene datos de precios de autos y stock. 
Construye el código necesario que emita el precio mínimo, el máximo y promedio.
"""
from statistics import median
import pandas as pd

def main():

    # Permite acceder a un archivo xlsx
    xls = pd.ExcelFile('Clases/Unsam.Clase.6/dataset/14.autos.xlsx')
    #print(xls.sheet_names) # parsea las hojas del excel

    cars = xls.parse('autos') # Parsea la hoja autos
   
    minPrice = int(cars['PRECIO'].min())
    sum = int(cars['PRECIO'].sum())
    total = int(cars['PRECIO'].count())
    averagePrice = round(sum/total)
    maxPrice = int(cars['PRECIO'].max())
    
    print(f'El Precio minimo es: {minPrice}')
    print(f'El Precio promedio es: {averagePrice}')
    print(f'El Precio maximo es: {maxPrice}')



if __name__ == '__main__':
    main()
