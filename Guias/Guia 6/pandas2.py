"""
2.Escribe una función que reciba un diccionario con las notas de los alumnos de curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica de cada uno.
"""

import pandas as pd
import numpy as np

def main():

    def toSerie(dic):
        #Genero matri con min, max, media y desviacion std
        matriz = np.min(list(dic.values()),axis=1)
        #Vstack apila matrices verticalmente hstack 
        matriz = np.vstack([matriz, np.max(list(dic.values()),axis=1)])
        matriz = np.vstack([matriz, np.round(np.mean(list(dic.values()),axis=1),decimals=2)])
        matriz = np.vstack([matriz, np.round(np.std(list(dic.values()),axis=1),decimals=2)])
        matriz = np.swapaxes(matriz,0,1)
        #Genero panda Series con los valores a retornar
        data = pd.Series(list(matriz), index=dic.keys(), dtype=np.float64)
        return data

    grades = {
        'facundo': [1,10,5,7],
        'charly': [10,9,8,7]
    }

    my_dataFrame = toSerie(grades)
    print(f'\n{my_dataFrame}')

if __name__ == '__main__':
    main()
