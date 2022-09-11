#7. Usa el diagrama de Venn para determinar el número de elementos en cada conjunto descrito en los problemas.
from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "A", "B", "C"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    diagram.get_label_by_id('100').set_text('3')
    diagram.get_label_by_id('010').set_text('8')
    diagram.get_label_by_id('001').set_text('12')
    diagram.get_label_by_id('110').set_text('7')
    diagram.get_label_by_id('011').set_text('4')
    diagram.get_label_by_id('101').set_text('8')
    diagram.get_label_by_id('111').set_text('8')

    plt.text(0.50, -0.65, s='6', size=14)

    plt.show()
if __name__ == '__main__':
    main()
