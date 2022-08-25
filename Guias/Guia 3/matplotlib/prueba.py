"""
1. Se tiene la siguiente información correspondiente al PIB de países latinoamericanos (en millones de dólares), información revisada al 15/DIC/2020, fuente: [A] CEPAL: Comisión Económica para América Latina y el Caribe - Estimaciones propias con base en fuentes oficiales, que se puede obtener en: https://estadisticas.cepal.org/cepalstat/tabulador/ConsultaIntegrada.asp?IdAplicacion=6&idTema=131&idIndicador=2204&idioma=e
Crea las listas con los datos y genera un gráfico de barras que visualice la información claramente.
"""
import matplotlib.pyplot as plt

def main():
    #Inicializar un objeto figura
    fig = plt.figure()

    #Agregue un objeto Axes a la figura usando add_subplot(1,1,1)
    #(1,1,1) aca le dice que agregue una cuadricula de 1x1, 1ra subtrama
    ax = fig.add_subplot(1,1,1)

    x = [1, 2, 3]
    y = [1, 2, 3]

    #Trazar los datos y mostrarlos
    ax.plot(x, y) #CON FORMATO LINEAL

    plt.show()

if __name__ == "__main__":
    main()



