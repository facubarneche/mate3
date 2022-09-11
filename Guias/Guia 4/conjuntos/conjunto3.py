"""
3.En una escuela de 500 estudiantes, hay:
- 125 estudiantes inscriptos en Álgebra II,
- 275 estudiantes que practican deportes y
- 52 estudiantes que están inscriptos en Álgebra II y practican deportes.
Crea un diagrama de Venn para ilustrar esta información.
Solución: Primero, establezcamos que el conjunto representa los estudiantes inscritos en Álgebra II y el conjunto representa los estudiantes que practican deportes. Generalmente hablando, es más fácil empezar en el centro o en la "intersección" del diagrama de Venn. Una vez que ubicamos 52 en la intersección, podemos restarlo al número total de estudiantes que practican deporte y al número total de estudiantes inscriptos en Álgebra II para determinar cuántos solo hacen una actividad o la otra. Finalmente, podemos restar este total a 500 para encontrar cuántos están completamente fuera de los círculos.
"""

from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():
    U=500
    
    v = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('A', 'B'))
    v.get_patch_by_id('10').set_alpha(0.5)
    v.get_patch_by_id('10').set_color('tomato')
    v.get_patch_by_id('01').set_alpha(0.5)
    v.get_patch_by_id('01').set_color('tomato')
    v.get_patch_by_id('11').set_alpha(0.5)
    v.get_patch_by_id('11').set_color('orange')
    v.get_label_by_id('10').set_text('125 - 52 = 73')
    v.get_label_by_id('01').set_text('257 - 52 = 205')
    v.get_label_by_id('11').set_text('52')

    plt.text(-0.70, 0.52,
    s="Universo = " + str(f'{U}'),
    size=10,ha="left",va="top",bbox=dict(boxstyle="square", # tipo de cuadro
    ec=(1.0, 0.7, 0.5),
    fc=(1.0, 0.9, 0.8),))
    
    plt.annotate('Inscriptos en\nÁlgebra II: 125', xy = v.get_label_by_id('10').get_position(), xytext = (-50,-80), size = 'medium', ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0', fc = 'lime', alpha = 0.3), arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = 0.2', color = 'gray'))
    
    plt.annotate('Practican\ndeportes: 257', xy = v.get_label_by_id('01').get_position(), xytext = (50,-80), size = 'medium', ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0', fc = 'lime', alpha = 0.3),arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = -0.2', color = 'gray'))

    plt.annotate('Inscritos en Álgebra II\ny practican deportes.', xy = v.get_label_by_id('11').get_position(), xytext = (0,-70), size = 'medium', ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3),
    arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad = 0',color = 'gray'))
    
    # Valor de los que quedan afuera
    plt.text(0.28, -0.65,
    s="Fuera de\nlos conjuntos = " + str('500-(73+52+205)=170'),
    size=10)
    # plt.axis('on')
    plt.show()

if __name__ == '__main__':
    main()
