"""
10.
Se encuesta a 150 familias consultando por el nivel educacional actual de sus hijos.
Los resultados obtenidos son:
▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.
▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria
▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.
▪ 22 familias tienen hijos en Enseñanza Media y Universitaria.
▪ 72 familias tienen hijos en Enseñanza Media.
▪ 71 familias tienen hijos en Enseñanza Básica.
▪ 38 familias tienen hijos en Enseñanza Universitaria.
Con la información anterior, deducir:
a. El número de familias que solo tienen hijos universitarios.
b. El número de familias que tienen hijos solo en dos nivele
"""

from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():

    #Universo = 150 familias
    #Resto = 27 familias
    BMU = 10   
    BU = 16
    BM = 30
    MU = 22
    M = 72
    B = 71
    U = 38

    #Devuelve el valor de un grupo el cual tiene 2 niveles de enseñenzas
    def only2(level1):
        return level1 - BMU
    #FinDef
  
    #Devuelve el valor de un grupo el cual tiene 1 nivel de enseñanza
    def only1(level1, level2, level3):
        return level1 - ( only2(level2) + only2(level3) + BMU ) 
    #FinDef

    #*************************Respuestas:******************************#

    #a. El número de familias que solo tienen hijos universitarios.
    print(f'El numero de familias que tienen hijos solo con nivel universitarios es: {only1(U, MU, BU)}')
    
    #b. El número de familias que tienen hijos solo en dos niveles
    print(f'El numero de familias que tienen hijos solo en 2 niveles son: {only2(BM) + only2(MU) + only2(BU)}')

    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Basica", "Media", "Universitaria"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    diagram.get_label_by_id('100').set_text(only1(B, BM, BU))   #Enseñanza Basica
    diagram.get_label_by_id('010').set_text(only1(M, BM, MU))   #Enseñanza Media
    diagram.get_label_by_id('001').set_text(only1(U, MU, BU))   #Enseñanza Universitaria
    diagram.get_label_by_id('110').set_text(only2(BM))          #Enseñanza Basica y Media
    diagram.get_label_by_id('011').set_text(only2(MU))          #Enseñanza Media y Universitaria
    diagram.get_label_by_id('101').set_text(only2(BU))          #Enseñanza Basica y Universitaria
    diagram.get_label_by_id('111').set_text(BMU)                #Enseñanza Basica, Media y Universitaria

    plt.text(0.50, -0.65, s='', size=14)

    plt.show()



if __name__ == '__main__':
    main()
