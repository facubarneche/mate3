"""
2. Resolver con numpy. Calcular la suma de los elementos de a (ejercicio anterior) utilizando dos fors anidados
suma = 0
IMPLEMENTAR
print(suma)
Calcular la suma de los elementos de a utilizando np.sum
IMPLEMENTAR
Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
promedio=0
IMPLEMENTAR
print(promedio)
Calcular el promedio de los elementos de las primeras dos filas de utilizando slices (notación (:)) y np.mean
IMPLEMENTAR
"""

import numpy as np

def main():

    lista_de_listas =[ [-44,12], [12.0,51], [1300, -5.0]]

    a = np.array(lista_de_listas)
    suma = 0

    for i in a:
        for j in i:
            suma += j

    print('Suma con fors')
    print(suma)

    print('Suma con np.sum()')
    print(a.sum())

    print('Promedio con fors')
    prom = 0
    count = 0

    for i in a:
        if count == 4:
            break

        for j in i:
            count += 1
            prom += j

    print(prom / count)

    print('Promedio con notacion np')
    print(np.mean(a[0:2, :]))

if __name__ == '__main__':
    main()
