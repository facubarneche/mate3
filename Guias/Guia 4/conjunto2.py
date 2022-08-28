"""
2.En una escuela de 600 alumnos, 100 no estudian ningún idioma extranjero, 450 estudian francés y 50 estudian francés e inglés. ¿Cuántos estudian solo inglés?
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

def main():

    students = 600
    french = 450
    french_english = 50
    no_language = 100

    #################################################################################
    # Gráfico de resultados
    #################################################################################
    # preparamos la ventana del gráfico
    plt.figure('Ejercicio 2 conjunto')

    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
        "Frances", "Ingles", "Ninguno"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(10)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text(french - french_english)
    diagram.get_label_by_id('010').set_text(students - french - french_english)
    diagram.get_label_by_id('001').set_text(no_language)
    diagram.get_label_by_id('110').set_text(french_english)
    diagram.get_label_by_id('011').set_text(0)
    diagram.get_label_by_id('101').set_text(0)
    diagram.get_label_by_id('111').set_text(0)

    plt.show()

if __name__ == '__main__':
    main()
