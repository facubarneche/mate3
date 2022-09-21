from functools import total_ordering
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

#Recuperatorio Primer Parcial Mate III |28-5-2021

"""
En una encuesta a personas que tienen mascotas, dónde debían destacar las principales
características, se determinó que:
*55 son juguetones y son muy compañeros.
*48 son muy compañeros y son inteligentes.
*120 son juguetones e inteligentes.
*40 son juguetones, inteligentes y son muy compañeros.
Los datos se recabaron de la siguiente manera:
juguetones = (9, 25, 27, 38, 13, 6, 42)
inteligentes = [10, 8, 38, 42, 13, 27]
compañeros = {'a':27,'b':6, 'c':13, 'd':8, 'e':9,'f':5}
Responder:
a. ¿Cuántas mascotas son inteligentes solamente?
b. ¿Cuántas mascotas son sólo juguetones?
c. ¿Cuántas mascotas sólo son muy compañeros?
d. ¿Cuántas mascotas sólo son juguetones e inteligentes?
e. ¿Cuántas mascotas sólo son juguetones y son muy compañeros?
f. ¿Cuántas mascotas sólo son inteligentes y son muy compañeros?
g. Calcular el conjunto universal
A modo de sugerencia se indican los pasos ordenados para la solución:
# 1. declaraciones
# 2. definir funciones de control (opcional) y otras (necesarias)
# 3. convertir en set las estructuras
# 4. Resolver las preguntas y el resto de operaciones para armar el gráfico
# 5. Definir diagrama de Venn, gráfico y respuestas.
"""

def main():
    ##################################################################################
    # Declaraciones
    ##################################################################################
    
    juguetones = (9, 25, 27, 38, 13, 6, 42)
    inteligentes = [10, 8, 38, 42, 13, 27]
    compañeros = {'a':27,'b':6, 'c':13, 'd':8, 'e':9,'f':5}

    ##################################################################################
    # Seteo las variables
    ##################################################################################

    setJuguetones = set(juguetones)
    setInteligentes = set(inteligentes)
    setCompañeros = set(compañeros.values())

    #Suponemos que no queda ninguno fuera del conjuntos
    universal = sum(setJuguetones | setInteligentes | setCompañeros)
    ninguno = 0

    #Compruebo que sean sets y sus valores
    print(f'setJuguetones => {setJuguetones}, tipo => {type(setJuguetones)}')
    print(f'setInteligentes => {setInteligentes}, tipo => {type(setInteligentes)}')
    print(f'setCompañeros => {setCompañeros}, tipo => {type(setCompañeros)}')

    ##################################################################################
    # Funciones y Operaciones
    ##################################################################################
        
    def all(atr1, atr2, atr3):
        return atr1 & atr2 & atr3

    def only2(atr1, atr2):
        return (atr1 & atr2)

    def only1(atr1, atr2, atr3):
        return (atr1 - atr2) & (atr1 - atr3)

    j_i = only2(setJuguetones, setInteligentes, )
    i_c = only2(setInteligentes, setCompañeros)
    j_c = only2(setJuguetones, setCompañeros)
    j_i_c = all(setJuguetones, setInteligentes, setCompañeros)
    j = only1(setJuguetones, setInteligentes, setCompañeros)
    i = only1(setInteligentes, setJuguetones, setCompañeros)
    c = only1(setCompañeros, setJuguetones, setInteligentes)

    print(f'Juguetones e Inteligentes => {j_i}')
    print(f'Inteligentes y Compañeros => {i_c}')
    print(f'Juguetones y Compañeros => {j_c}')
    print(f'Juguetones, Inteligentes y Compañeros => {j_i_c}')

    total_j_i_c = sum(j_i_c)
    total_j_i = sum(j_i) - total_j_i_c
    total_i_c = sum(i_c) - total_j_i_c 
    total_j_c = sum(j_c) - total_j_i_c
    total_j = sum(j)
    total_i = sum(i)
    total_c = sum(c)
    
    ##################################################################################
    # Gráfico de resultados
    ##################################################################################
    # preparamos la ventana del gráfico
    plt.figure('Ejemplo de primer parcial ')
    
    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
        "Juguetones", "Compañeros", "Inteligentes"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(10)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text(total_j)
    diagram.get_label_by_id('010').set_text(total_c)
    diagram.get_label_by_id('001').set_text(total_i)
    diagram.get_label_by_id('110').set_text(total_j_c)
    diagram.get_label_by_id('011').set_text(total_i_c)
    diagram.get_label_by_id('101').set_text(total_j_i)
    diagram.get_label_by_id('111').set_text(total_j_i_c)

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
            s="Solo inteligentes = " + str(total_i),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.40,
            s="Solo juguetones = " + str(total_j),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.50,
            s="Solo compañeros = " + str(total_c),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.60,
            s="sólo son juguetones e inteligentes = " + str(total_j_i),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.70,
            s="sólo son juguetones y son compañeros = " + str(total_j_c),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.80,
            s="sólo son inteligentes y son compañeros = " + str(total_i_c),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.90,
            s="Universo = " + str(universal),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.axis('on')  # Recuadro
    plt.title("Deportistas")
    plt.show()
    ##################################################################################
    # Fin de programa
    ##################################################################################

if __name__ == '__main__':
    main()
