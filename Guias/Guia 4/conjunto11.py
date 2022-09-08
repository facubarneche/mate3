"""
11. Una encuesta sobre 500 estudiantes inscriptos en una o más asignaturas de Matemática, Física y Química durante un semestre, reveló los siguientes números de estudiantes en los cursos indicados: Matemática 329, Física 186, Química 295, Matemática y Física 83, Matemática y Química 217, Física y Química 63. Cuántos alumnos estarán inscriptos en:
a) Los tres cursos
b) Matemática pero no Química
c) Física pero no matemáticas, Química pero no Física
e) Matemática o Química, pero no Física
f) Matemática y Química, pero no Física
g) Matemática pero no Física ni Química
"""


from matplotlib_venn import *
from matplotlib import pyplot as plt

def main():

    U = 500 #500 estudiantes inscriptos en 1 o mas asignaturas
    mate = 329
    fis = 186
    qui = 295
    mate_y_fis = 83
    mate_y_qui = 217
    fis_y_qui = 63


    def only1(mat1, mat2, union_mat1_mat2):
        return U - (mat1 + mat2 - union_mat1_mat2)
    #finDef

    def inters(mat1, inter):
        return mat1 - inter
    #finDef

    def every():
        return mate - only1(fis, qui, fis_y_qui) - (inters(qui, fis_y_qui) - only1(mate, fis, mate_y_fis)) - (inters(mate, mate_y_qui) - only1(fis, qui, fis_y_qui))
    #finDef

    #################################################################################
    # Gráfico de resultados
    #################################################################################

    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Matemática", "Física", "Química"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(16)
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)

    #Al universo le resto la suma de fisica y quimica menos la interseccion de las mismas
    diagram.get_label_by_id('100').set_text(only1(fis, qui, fis_y_qui))
    #Al universo le resto la suma de matematica y quimica menos la interseccion de las mismas
    diagram.get_label_by_id('010').set_text(only1(mate, qui, mate_y_qui))
    #Al universo le resto la suma de matematica y fisica menos la interseccion de las mismas
    diagram.get_label_by_id('001').set_text(only1(mate, fis, mate_y_fis))
    #Mate total - interseccion mate y quimica y matematica solo antes resuelto
    diagram.get_label_by_id('110').set_text(inters(mate, mate_y_qui) - only1(fis, qui, fis_y_qui))    #Fisica total - interseccion mate y fisica y fisica solo antes resuelto
    diagram.get_label_by_id('011').set_text(inters(fis, mate_y_fis) - only1(mate, qui, mate_y_qui))
    #quimica total - interseccion fisica y quimica y quimica solo antes resuelto
    diagram.get_label_by_id('101').set_text(inters(qui, fis_y_qui) - only1(mate, fis, mate_y_fis))
    #Le resto arbitrariamente una materia menos las 2 intersecciones con las otras 2 materias
    diagram.get_label_by_id('111').set_text(every())

    plt.text(0.50, -0.65, s='', size=14)

    plt.show()


if __name__ == '__main__':
    main()
