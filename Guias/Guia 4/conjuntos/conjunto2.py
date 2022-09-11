"""
2.En una escuela de 600 alumnos, 100 no estudian ningún idioma extranjero, 450 estudian francés y 50 estudian francés e inglés. ¿Cuántos estudian solo inglés?
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def main():

    students = 600
    french_english = 50
    french = 450 - french_english
    no_language = 100

    #################################################################################
    # Gráfico de resultados
    #################################################################################
    # preparamos la ventana del gráfico
    plt.figure('Ejercicio 2 conjunto')

    # establecemos el tamaño de la fuente
    diagram = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('Frances', 'Ingles'))
    
    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('10').set_text(french)
    diagram.get_label_by_id('01').set_text(students - (french + french_english + no_language))
    diagram.get_label_by_id('11').set_text(french_english)

    plt.show()

if __name__ == '__main__':
    main()
