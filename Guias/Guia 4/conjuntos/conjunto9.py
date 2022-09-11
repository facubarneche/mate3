"""
9. En una encuesta realizada en la ciudad de Buenos Aires, acerca de los medios de transporte más utilizados entre colectivos, subte o moto, se obtuvieron los siguientes resultados: de los 3200 encuestados, 1950 utilizan el subte, 400 se desplazan en moto, 1500 van en colectivo, 800 se desplazan en colectivo y subte, además ninguno de los que se transporta en moto utiliza colectivo o subte.

a. El número de personas que solo utiliza el subte es….
b. Las persona que solo utilizan máximo 2 medios de transporte son…
"""
from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():

    U = 3200
    cole_subte = 800
    moto = 400
    subte = 1950
    cole = 1500

    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Colectivo", "Moto", "Subte"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    diagram.get_label_by_id('100').set_text(cole - cole_subte)
    diagram.get_label_by_id('010').set_text(moto)
    diagram.get_label_by_id('001').set_text(subte - cole_subte)
    diagram.get_label_by_id('110').set_text(0)
    diagram.get_label_by_id('011').set_text(0)
    diagram.get_label_by_id('101').set_text(cole_subte)
    diagram.get_label_by_id('111').set_text(0)

    plt.text(0.50, -0.65, s='', size=14)

    plt.show()



if __name__ == '__main__':
    main()
