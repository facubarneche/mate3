"""
1. Resolver con numpy. Dado:
lista_de_listas=[ [-44,12], [12.0,51], [1300, -5.0]]
a = np.array(lista_de_listas)
print("Matriz original")
print(a)
Restarle 5 a la fila 2 de la matriz IMPLEMENTAR print(a)
Multiplicar por 2 toda la matriz
IMPLEMENTAR
print(a)
Dividir por -5 las dos primeras filas de la matriz
IMPLEMENTAR
print(a)
Imprimir la última fila de la matriz
ultima_fila=0
IMPLEMENTAR
print(ultima_fila)
"""

import numpy as np

def main():

    lista_de_listas =[ [-44,12], [12.0,51], [1300, -5.0]]

    a = np.array(lista_de_listas)
    
    print('Matriz Original')
    print(a)

    print('Restarle 5 a la fila 2')
    a[2, :] = a[2, :] - 5
    print(a)

    print('Dividir por -5 las 2 primeras filas')
    a[0:2, :] = a[0:2, :] / -5
    print(a)

    print('Imprimir la ultima fila de la matriz')
    ultima_fila = 0

    ultima_fila = a[2,:]

    print(ultima_fila)

if __name__ == '__main__':
    main()
