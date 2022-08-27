"""
4. El propietario de una fábrica electrodomésticos, que opera una línea de producción, tiene dos productos principales y necesita un gráfico de barras comparativo, de diferentes colores para representar la producción de cada producto durante 5 días, lunes a viernes. El eje horizontal mostraría los días y el eje vertical las barras que representan la producción. Como datos tenemos:
prod1 = (20, 35, 30, 35, 27)
prod2 = (25, 32, 34, 20, 25)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

Podría representarse la diferencia de fabricación entre productos en el mismo gráfico?
"""

import matplotlib.pyplot as plt
import numpy as np

def main():

    prod1 = (20, 35, 30, 35, 27)
    prod2 = (25, 32, 34, 20, 25)
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

    #Convierto en array la tupla de productos
    prod1 = list(prod1)
    prod2 = list(prod2)
    
    datos_lins = np.array(prod1)
    datos_cuads = np.array(prod2)

    plt.figure()

    xvals = range(len(datos_lins))
    plt.bar(dias, prod1, width = 0.3)


    new_xvals = []
    for item in xvals:
        new_xvals.append(item+0.3)
    plt.bar(new_xvals, datos_cuads, width = 0.3 ,color='red')

    plt.show()

if __name__ == '__main__':
    main()
