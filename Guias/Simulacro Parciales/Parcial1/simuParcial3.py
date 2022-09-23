from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def main():
    """
    En en una escuela de 1000 alumnos, se han evaluado literatura, matemática y biología, obte-
    niéndose los siguientes resultados:
    680 aprobaron literatura. Los datos de la evaluación de Literatura se registraron en un
    diccionario:
    Literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
    "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}
    320 aprobaron biología. Los datos de la evaluación de Biología se registraron en una tupla:
    Biologia = (40, 50, 60, 75, 34, 61)
    490 aprobaron matemática. Los datos de la evaluación de Matemática se registraron en una
    lista:
    Matematica = [34, 40, 61, 75, 87, 90, 103]
    Responder:
    a. cuántos aprobaron biología matemática y literatura.
    b. cuántos aprobaron sólo literatura y matemática?
    c. cuántos aprobaron sólo literatura?
    d. cuántos aprobaron solo biología?
    e. cuántos aprobaron sólo matemática?
    f. cuántos aprobaron 2 de los 3 exámenes?
    """
    
    universal = 0
    ninguno = 0

    ##################################################################################
    # Gráfico de resultados
    ##################################################################################
    # preparamos la ventana del gráfico
    plt.figure('Ejemplo de primer parcial ')
    
    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
        "label1", "label2", "label3"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(10)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text('100')
    diagram.get_label_by_id('010').set_text('010')
    diagram.get_label_by_id('001').set_text('001')
    diagram.get_label_by_id('110').set_text('110')
    diagram.get_label_by_id('011').set_text('011')
    diagram.get_label_by_id('101').set_text('101')
    diagram.get_label_by_id('111').set_text('111')

    # marcamos los contornos
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

    # agregamos más datos aclaratorios al gráfico
    plt.text(-0.90, 0.67,      # Texto y cantidad universal
            f"Universal = {universal}",
            size=10)

    plt.text(0.40, -0.5,      # Texto fuera del conjunto
            f"Fuera\nde los\nconjuntos = {ninguno}",
            size=8)

    # Respondemos las preguntas
    plt.text(-1.10, -0.20,
            s="Respuestas solicitadas: ",
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.30,
            s="Condicion 1 = " + str('Condicion' ),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.40,
            s="Condicion 2 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.50,
            s="Condicion 3 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.60,
            s="Condicion 4 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.70,
            s="Condicion 5 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.80,
            s="Condicion 6 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.90,
            s="Condicion 7 = " + str('Condicion'),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.axis('on')  # Recuadro
    plt.title("Title")
    plt.show()
    ##################################################################################
    # Fin de programa
    ##################################################################################


if __name__ == '__main__':
    main()
