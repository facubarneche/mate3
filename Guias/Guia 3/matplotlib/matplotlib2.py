"""
1. Se tiene la siguiente información correspondiente al PIB de países latinoamericanos (en millones de dólares), información revisada al 15/DIC/2020, fuente: [A] CEPAL: Comisión Económica para América Latina y el Caribe - Estimaciones propias con base en fuentes oficiales, que se puede obtener en: https://estadisticas.cepal.org/cepalstat/tabulador/ConsultaIntegrada.asp?IdAplicacion=6&idTema=131&idIndicador=2204&idioma=e
Crea las listas con los datos y genera un gráfico de barras que visualice la información claramente.
"""
import matplotlib.pyplot as plt

def main():

    #Tabla de paises
    country = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guayana', 'México', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']
    #Tabla de PBIs
    pib = [440769.2, 29702.8, 2364409.9, 286013.8, 394571.1, 88554.7, 4780.6, 1309880.9, 37260.6, 210881.6, 4678.2, 50532.1, 116067.8]

    fig = plt.figure() #Creamos la figura
    ax = fig.add_subplot(1, 1, 1)   #Creamos los objetos Axes

    ax.pie(pib, labels = country, autopct = "%0.1f %%")

    plt.show()

if __name__ == '__main__':
    main()
