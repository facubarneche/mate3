"""
3. Generar una matriz de 7 por 9. Las primeras 3 columnas de la matriz tienen que tener el valor 0. La cuarta columna debe tener el valor 0.5, excepto por el último valor de esa columna, que tiene que ser 0.7. Las otras tres columnas deben tener el valor 1. Luego imprimir la matriz.
Imprimir también el promedio de la última fila.
"""
import numpy as np

def main():
    #Llena 9 por 3 de ceros
    matrizCeros = np.zeros((9,3))

    #Lleno un array de 8 posiciones con todo 0.5
    array = np.full(8, fill_value= 0.5)

    #Creo 1 nuevo array y le concateno al anterior solo un 0.7
    array2 = np.append(array, 0.7)

    #Le doy forma para que coincida con los 0 y unos
    array2.shape = (9,1)

    #Llena 9 por 3 de unos
    matrizUnos = np.ones((9,3))

    #Contatena las 2 matrices, axis = 1 es para que concatene a lo largo de la matriz
    #Axis por default = 0, concatena abajo de la matriz
    matriz = np.concatenate([matrizCeros, array2, matrizUnos], axis = 1)

    print(matriz)


if __name__ == '__main__':
    main()
