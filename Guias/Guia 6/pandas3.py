"""
3.Escribe una función que reciba los datos siguientes en un DataFrame, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
"""

import pandas as pd


def main():

    datos = {
        'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
        'Ventas':[30500, 35600, 28300, 33900], 
        'Gastos':[22000, 23400, 18100, 20700]
        }

    def balance(data):    
        s = pd.Series(data)
        value = pd.DataFrame({'ventas': s[1], 'gastos': s[2]}, pd.Series(s[0]))
        value['balance'] = value['ventas'] - value['gastos']
        return value
    #FinDef

    bal = balance(datos)
    print(bal)

if __name__ == '__main__':
    main()
