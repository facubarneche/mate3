"""
3.Los siguientes datos de población y superficie pertenecen a países de América y el Caribe. Genera un gráfico que muestre la relación entre población y superficie. Fuente: https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_de_Am%C3%A9rica_por_poblaci%C3%B3n
https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_de_Am%C3%A9rica_por_superficie
"""
import matplotlib.pyplot as plt

def main():

    #Tabla de paises
    country = ['Estados Unidos', 'Brasil','México','Colombia', 'Argentina', 'Canada', 'Perú','Venezuela', 'Chile', 'Guatemala', 'Ecuador', 'Bolivia', 'Cuba', 'Haiti', 'Republica Dominicana', 'Honduras','Paraguay', 'Nicaragua', 'El salvador', 'Costa Rica', 'Panamá', 'Uruguay', 'Jamaica', 'Puerto Rico', 'Trinida y Tobago', 'Guyana', 'Surinam', 'Belice', 'Bahamas', 'Barbados', 'Santa Lucia', 'Granada', 'San Vicente y las Granadinas', 'Antigua y Barbuda', 'Dominica', 'San Cristóbal y Nieves']

    #Tabla de Poblaciones
    population = [331002651, 212559417, 128932753, 50882891, 45195774, 37742154, 33050325, 28435940, 19116201, 17915568, 17643054, 11673021, 11326616, 11402528, 10847910, 9904607, 7132538, 6624554, 6486205, 5094118, 4314767, 3473730, 2961167, 2860853, 1399488, 786552, 586632, 397628, 393244, 287375, 183627, 112523, 110940, 97929, 71989, 53199]

    #Tabla de Superficies
    surface = [9498193, 8514877, 1964375, 1141748, 2792600, 9984670, 1285216, 916445, 755934, 108990, 283561, 1098585, 110860, 27850, 48762, 112492, 406750, 121430, 21481, 51160, 78260, 176215, 11524, 9104, 5128, 214969, 163820, 22966, 13940, 439, 623, 344, 389, 443, 754, 261]

    relation = []

    for i in range(len(population)):
        relation.append(population[i] / surface[i])

    fig = plt.figure() #Creamos la figura
    ax = fig.add_subplot(1, 1, 1)   #Creamos los objetos Axes
    ax.set_title('Relacion de los paises respecto a su superficie y su poblacion') #Creamos un titulo

    ax.pie(relation, labels = country, autopct = "%0.1f %%")

    plt.show()

if __name__ == '__main__':
    main()
