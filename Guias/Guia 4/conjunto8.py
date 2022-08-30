"""
8. En una encuesta de 80 dueños de casa, se descubrió que:
30 tenían al menos un perro.
42 tenían al menos un gato.
21 tenían al menos una mascota "otra" (pez, tortuga, reptil, hámster, etc.).
20 Tenían perro(s) y gato (s).
10 tenían gato(s) y mascota(s) otra.
8 tenían perro(s) y mascota(s) otra.
5 tenían los tres tipos de mascotas.
Haz un diagrama de Venn para ilustrar los resultados de la encuesta y responde:

a.¿Cuántos tenían perro(s) y gato(s) pero no mascota(s) "otra"?
b.¿Cuántos solo tenían perro(s)?
c.¿Cuántos no tenían mascotas?
d.¿Cuántos dueños de mascota(s) otra también tenían perro(s) o gato(s), pero no ambos?
Puedes utilizar las letras en el siguiente diagrama de Venn para describir la región de cada uno de los conjuntos.
"""

from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():
    plt.figure('Ejercicio 8 conjunto')

    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Perro", "Gato", "Otra"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    diagram.get_label_by_id('100').set_text('a')
    diagram.get_label_by_id('010').set_text('b')
    diagram.get_label_by_id('001').set_text('c')
    diagram.get_label_by_id('110').set_text('20')
    diagram.get_label_by_id('011').set_text('10')
    diagram.get_label_by_id('101').set_text('8')
    diagram.get_label_by_id('111').set_text('5')

    plt.show()
if __name__ == '__main__':
    main()
