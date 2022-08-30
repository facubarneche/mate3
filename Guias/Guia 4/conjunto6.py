"""
6.
Crea un diagrama de Venn para representar la información siguiente y responder las preguntas:
En una encuesta a 15 estudiantes secundarios, se descubrió que:
•80 estudiantes tienen laptops.
•110 estudiantes tienen celulares.
•125 estudiantes tienen iPod
•62 estudiantes tienen una laptop y un celular.
•58 estudiantes tienen una laptop y un iPod.
•98 estudiantes tienen un celular y un iPod.
•50 estudiantes tienen los tres objetos.
Responde:
a. ¿Cuántos estudiantes tienen solo un celular?
b. ¿Cuántos estudiantes no tienen ninguno de los objetos mencionados?
c. ¿Cuántos estudiantes tienen un iPod y una laptop, pero no un celular?
Solución: Primero, usaremos la información dada para construir el diagrama de Venn, como se muestra a continuación:
Podemos comenzar con escribir 50 en el centro, donde los estudiantes tienen los 3 objetos. Luego, podemos encontrar los valores en azul al restar 50 de cada uno de los valores "superpuestos". Por ejemplo, hay 62 estudiantes con una laptop y un celular y 50 de ellos también tienen un iPod. Para encontrar el número de los que tienen laptop y celular pero no iPod, resta 62 - 50 = 12 . Una vez que encuentres los valores azules, podemos encontrar los valores verdes al restar los valores azules y rojos en cada subconjunto del total en el subcon
junto. Por ejemplo, el número de estudiantes con un celular pero no otro objeto tecnológico es 110 - (50 + 12 + 48) = 0. Finalmente, podemos sumar todos los valores en los círculos y restar esto de 150, el número de estudiantes encuestados, para determinar que 3 estudiantes no tienen ninguno de estos objetos.
"""
from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():

    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Laptop", "Celular", "Ipod"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text('10')
    diagram.get_label_by_id('100').set_color('green')
    diagram.get_label_by_id('010').set_text('0')
    diagram.get_label_by_id('010').set_color('green')
    diagram.get_label_by_id('001').set_text('19')
    diagram.get_label_by_id('001').set_color('green')
    diagram.get_label_by_id('110').set_text('12')
    diagram.get_label_by_id('110').set_color('blue')
    diagram.get_label_by_id('011').set_text('48')
    diagram.get_label_by_id('011').set_color('blue')
    diagram.get_label_by_id('101').set_text('8')
    diagram.get_label_by_id('101').set_color('blue')
    diagram.get_label_by_id('111').set_text('50')
    diagram.get_label_by_id('111').set_color('red')

    plt.text(0.50, -0.65, s='3',size=14)

    plt.show()

    """
    Ahora que el diagrama de Venn está completo, podemos utilizarlo para responder las preguntas.
    a. Hay 0 estudiantes que solo tienen un celular.
    b. Hay 3 estudiantes con ningún objeto tecnológico mencionado.
    c. Hay 8 estudiantes con un iPod y una laptop pero no un celular.
    """

if __name__ == '__main__':
    main()
