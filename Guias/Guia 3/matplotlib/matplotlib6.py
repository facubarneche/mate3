"""
6.Traza un gráfico de dispersión (puntos) de los siguientes datos que representan las calificaciones de dos grupos de deportistas dentro de un rango (eje x). Identifica los valores de cada grupo con un color distinto.
grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

from cProfile import label
import matplotlib.pyplot as plt

def main():

    grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    plt.figure()
    plt.scatter(rango, grupo1, label = 'Grupo 1', c='red')
    plt.scatter(rango, grupo2, label = 'Grupo 2', c='green')
    plt.xlabel('Rango')
    plt.ylabel('Calificaciones')
    plt.title('Calificaciones')
    plt.legend(loc="lower left",title='Leyenda', bbox_to_anchor=(0.8,1.0))

    plt.show()

if __name__ == "__main__":
    main()
