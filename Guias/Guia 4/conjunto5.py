"""
5. Crea un diagrama de Venn para ilustrar la información siguiente acerca de los subconjuntos M y N en el universo U: n(M) = 89; n(N ) = 103; n(M U N ) = 130; n(U ) = 178
Solución: De nuevo, comenzaremos en el medio de la intersección. Debemos determinar cuántos elementos hay en la intersección. Consideremos que cuando agregamos elementos M a los elementos en N, agregamos los elementos
de la intersección 2 veces. Esto sucede porque se cuentan en el conjunto M y también en N. Observaste que:
- n(M) + n(N ) = 89 + 103 = 192
mientras el:
- n(M U N ) = 130
Hemos contado 2 veces los 62 (192-130) elementos en M ∩ N. Ahora podemos poner este número en el diagrama y resolver como en el ejemplo anterior.
"""

from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():
    U=178
    v = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('M', 'N'))
    v.get_patch_by_id('10').set_alpha(0.5)
    v.get_patch_by_id('10').set_color('tomato')
    v.get_patch_by_id('01').set_alpha(0.5)
    v.get_patch_by_id('01').set_color('tomato')
    v.get_patch_by_id('11').set_alpha(0.5)
    v.get_patch_by_id('11').set_color('orange')
    v.get_label_by_id('10').set_text('89 - 62 = 27')
    v.get_label_by_id('01').set_text('103 - 62 = 41')
    v.get_label_by_id('11').set_text('62')

    plt.text(-0.70, 0.52,
    s="Universo = " + str(f'{U}'),
    size=10,ha="left",va="top",bbox=dict(boxstyle="square", # tipo de cuadro
    ec=(1.0, 0.7, 0.5),
    fc=(1.0, 0.9, 0.8),))

    plt.text(0.28, -0.65,
    s="Fuera de\nlos conjuntos = " + str('178-(27+62+41)=48'),
    size=10)
    # plt.axis('on')
    plt.show()

if __name__ == '__main__':
    main()

