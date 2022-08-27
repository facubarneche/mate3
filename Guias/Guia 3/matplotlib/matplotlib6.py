"""
6.Traza un gráfico de dispersión (puntos) de los siguientes datos que representan las calificaciones de dos grupos de deportistas dentro de un rango (eje x). Identifica los valores de cada grupo con un color distinto.
grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

import matplotlib.pyplot as plt

def main():

    grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    zip_generator=zip(grupo1, grupo2)
    x,y=zip(*zip_generator)
    plt.figure()
    
    plt.scatter(x[:2],y[:2],s=100,c='red',label='grupo 1')
    plt.scatter(x[2:],y[2:],s=100,c='green',label='grupo 2')
    plt.xlabel('Experiencia en años')
    plt.ylabel('Ingresos obtenidos')
    plt.title('Calificaciones')
    plt.legend(loc=4,frameon=False,title='Leyenda')

    plt.show()

if __name__ == "__main__":
    main()
