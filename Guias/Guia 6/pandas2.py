"""
2.Escribe una función que reciba un diccionario con las notas de los alumnos de curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica de cada uno.
"""

import pandas as pd

def main():

    gradesDictionary = {
        'facundo' : 7,
        'carlitos' : 10,
        'messi' : 10,
        'ivo cutzarida' : 3,
        'rodrigo' : 8,
        'jaimito' : 2
    }

    def notas(dictionary):
        array = []
        mini = min(dictionary.values())
        average = sum(dictionary.values()) / len(dictionary)
        maxi = max(dictionary.values())
        array = [mini, average, maxi]
        return array
    #FinDef

    data = notas(gradesDictionary)

    s = pd.Series(data)

    print(s)

if __name__ == '__main__':
    main()
