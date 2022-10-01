"""
4. La siguiente linea crea una matriz aleatoria de 5 por 5 con valores entre 0 y 1 
matriz_aleatoria = np.random.rand(5,5) print(matriz_aleatoria)
Imprimir las posiciones (Fila y columna) de los elementos de la matriz que son mayores que 0.5
"""

import numpy as np

def main():

    #Crea iun array 5x5 random y la imprime
    matriz_aleatoria = np.random.rand(5,5) 
    print(matriz_aleatoria, end='\n\n\n')

    #Devuelve un array con los mayores de 0.5 y la imprime
    x = matriz_aleatoria[matriz_aleatoria > 0.5]
    print(x)

    #Devuelve la misma matriz con true o false y la imprime
    print(matriz_aleatoria > 0.5, end='\n\n\n')

if __name__ == '__main__':
    main()
