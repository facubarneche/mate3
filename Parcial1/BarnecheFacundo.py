from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def main():

    """
    En una escuela de 1000 alumnos, se han evaluado literatura, matematica y biologia, obteniendose los siguientes resultados

    *680 aprobaron literatura y los datos se recolectaron en un diccionario: {"Romantica": 40, "Clasica":118, "Fantastica": 50, "Moderna": 95, "Antigua":56, "Poesia":131, "Cuento": 87, "Novela": 103}
    *320 aprobaron biologia y los datos se recolectaron en una tupla: (40, 50, 60, 75, 34, 61)
    *490 aprobaron matematica y los datos se recolectaron en una lista: [34, 40, 61, 75, 87, 90, 103]

    Responder:
    a. Cuantos aprobaron biologia, matematica y literatura?
    b. Cuantos aprobaron solo literatura y matematica?
    c. Cuantos aprobaron solo literatura?
    d. Cuantos aprobaron solo biologia?
    e. Cuantos aprobaron solo matematica?
    f. Cuantos aprobaron 2 de los 3 examenes?
    """
    
    ##################################################################################
    # Declaro variables y chequeo información recibida 
    ##################################################################################

    universal = 1000
    
    literatura = {
        "Romantica": 40,
        "Clasica":118, 
        "Fantastica": 50, 
        "Moderna": 95, 
        "Antigua":56, 
        "Poesia":131, 
        "Cuento": 87, 
        "Novela": 103
    }

    biologia = (40, 50, 60, 75, 34, 61)
    matematica = [34, 40, 61, 75, 87, 90, 103]

    #Funcion para sumar el contenido de la informacion dada y comprobar que es correcto
    def suma(materia):
        if type(materia) == dict:
            return sum(materia.values())
        else:
            return sum(materia)
    #FinDef

    #Asigno a nuevas variables la suma de la informacion para la comprobacion
    suma_literatura = suma(literatura)
    suma_biologia   = suma(biologia)
    suma_matematica = suma(matematica)

    #Compruebo con un print que la informacion sea correcta
    print('')
    print('Compruebo con un print que la informacion sea correcta', end='\n\n')
    print(f'Literatura deberia ser 680 => {suma_literatura}')
    print(f'Biologia deberia ser 320 => {suma_biologia}')
    print(f'Matematica deberia ser 490 => {suma_matematica}', end='\n\n')

    ##################################################################################
    # Pasar la información a sets 
    ##################################################################################

    #Pasa diccionarios, tuplas o listas a set
    def setter(materia):
        if type(materia) == dict:
            return set(materia.values())
        else:
            return set(materia)
    #FinDef

    #Asigno a nuevas variables la informacion recibida anteriormente pero como set
    set_literatura = setter(literatura)
    set_biologia   = setter(biologia)
    set_matematica = setter(matematica)

    #Compruebo con un print que las variables sean sets
    print('Compruebo con un print que las variables sean sets', end='\n\n')
    print(f'Literatura deberia ser un set => {type(set_literatura)} y sus valores son: {set_literatura}')
    print(f'Biologia deberia ser un set => {type(set_biologia)} y sus valores son: {set_biologia}')
    print(f'Matematica deberia ser un set => {type(set_matematica)} y sus valores son: {set_matematica}', end='\n\n')

    ##################################################################################
    # Calculos para obtener las respectivas intersecciones
    ##################################################################################

    #Obtiene la interseccion entre las 3 materias
    def lite_bio_mate(mat1, mat2, mat3):
        return mat1 & mat2 & mat3
    #FinDef

    #Obtiene la interseccion de 2 materias recibidas por parametro y le resta la interseccion de las 3 para no volver a contarla
    def inter2(mat1, mat2):
        return (mat1 & mat2) - l_b_m
    #FinDef

    #Obtiene solo los que aprobaron 1 materia, restandole las otras 2
    def solo1(mat1, mat2, mat3):
        return mat1 - mat2 - mat3
    #FinDef


    #Asigno a las variables los valores obtenidos
    l_b_m = lite_bio_mate(set_literatura, set_biologia, set_matematica)
    l_b = inter2(set_literatura, set_biologia)
    l_m = inter2(set_literatura, set_matematica)
    b_m = inter2(set_biologia, set_matematica)
    l = solo1(set_literatura, set_biologia, set_matematica)
    b = solo1(set_biologia, set_literatura, set_matematica)
    m = solo1(set_matematica, set_literatura, set_biologia)

    #Compruebo con un print el valor obtenido
    print('Compruebo con un print el valor obtenido', end='\n\n')
    print(f'Los alumnos que aprobaron literatura, biologia y matematica son: {l_b_m}')
    print(f'Los alumnos que aprobaron literatura y biologia son: {l_b}')
    print(f'Los alumnos que aprobaron literatura y matematica son: {l_m}')
    print(f'Los alumnos que aprobaron biologia y matematica son: {b_m}')
    print(f'Los alumnos que aprobaron literatura son: {l}')
    print(f'Los alumnos que aprobaron biologia son: {b}')
    print(f'Los alumnos que aprobaron matematica son: {m}', end='\n\n')


    ##################################################################################
    # Suma de conjuntos para obtener el total de alumnos aprobados
    ##################################################################################

    #Suma el conjunto recibido por parametro y devuelve la suma del mismo para luego colocar en el grafico
    #Recibe por parametro el conjunto obtenido en la funcion anterior 
    def sumarSets(materia):
        return sum(materia)
    #FinDef

    #Asigno a las variables los valores obtenidos
    total_l_b_m = sumarSets(l_b_m)
    total_l_b = sumarSets(l_b)
    total_l_m = sumarSets(l_m)
    total_b_m = sumarSets(b_m)
    total_l = sumarSets(l)
    total_b = sumarSets(b)
    total_m = sumarSets(m)

    #Compruebo con un print el valor obtenido
    print('Compruebo con un print el valor obtenido', end='\n\n')
    print(f'Los alumnos que aprobaron literatura, biologia y matematica son: {total_l_b_m}')
    print(f'Los alumnos que aprobaron literatura y biologia son: {total_l_b}')
    print(f'Los alumnos que aprobaron literatura y matematica son: {total_l_m}')
    print(f'Los alumnos que aprobaron biologia y matematica son: {total_b_m}')
    print(f'Los alumnos que aprobaron literatura son: {total_l}')
    print(f'Los alumnos que aprobaron biologia son: {total_b}')
    print(f'Los alumnos que aprobaron matematica son: {total_m}', end='\n\n')

    ##################################################################################
    # Respondo las preguntas 
    ##################################################################################

    """
    a. Cuantos aprobaron biologia, matematica y literatura?
    b. Cuantos aprobaron solo literatura y matematica?
    c. Cuantos aprobaron solo literatura?
    d. Cuantos aprobaron solo biologia?
    e. Cuantos aprobaron solo matematica?
    f. Cuantos aprobaron 2 de los 3 examenes?
    """

    #Devuelve solo los alumnos que aprobaron 2 de los 3 examenes para responder la pregunta f
    #Suma la interseccion de los 3 grupos y le hace la union, luego le resta la triple interseccion
    def preguntaF(mat1, mat2, mat3):
        return ((mat1 & mat2) | (mat1 & mat3) | (mat2 & mat3)) - l_b_m
    #FinDef

    #Suma todo el conjunto para devolver un unico valor
    def suma_dos_de_tres(param):
        return sum(param)
    #FinDef

    #Asigno una variable el valor obtenido
    #Si bien tengo los valores ya obtenidos y limpios, opte por usar las variables originales en set 
    # y comprobar que esta bien el resto
    dos_de_tres = preguntaF(set_literatura, set_biologia, set_matematica)

    total_dos_de_tres = suma_dos_de_tres(dos_de_tres)


    #Compruebo con un print el valor obtenido
    print(f'Compruebo con un print el valor obtenido', end='\n\n')
    print(f'a. Cuantos aprobaron biologia, matematica y literatura? => Los aprobados son {total_l_b_m} alumnos')
    print(f'b. Cuantos aprobaron solo literatura y matematica? => Los aprobados son {total_l_m} alumnos')
    print(f'c. Cuantos aprobaron solo literatura? => Los aprobados son {total_l} alumnos')
    print(f'd. Cuantos aprobaron solo biologia? => Los aprobados son {total_b} alumnos')
    print(f'e. Cuantos aprobaron solo matematica? => Los aprobados son {total_m} alumnos')
    print(f'f. Cuantos aprobaron 2 de los 3 examenes? => Los aprobados son {total_dos_de_tres} alumnos', end='\n\n')

    ##################################################################################
    # Calculos extras 
    ##################################################################################

    #Averiguo la cantidad de alumnos afuera de los 3 conjuntos
    fuera_del_conjunto = universal - (total_l + total_b + total_m + total_l_b + total_b_m + total_l_m + total_l_b_m)

    #Compruebo el valor obtenido
    print('Compruebo el valor obtenido de los alumnos fuera de los conjuntos', end='\n\n')
    print(f'Los alumnos que no aprobaron ninguna, (quedaron fuera de los conjuntos) son: {fuera_del_conjunto}', end='\n\n')


    ##################################################################################
    # Gráfico 
    ##################################################################################

    #Configuracion del grafico
    plt.figure('Parcial matematica III')
    
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=("Literatura", "Biologia", "Matematica"))

    diagram.get_label_by_id('100').set_text(total_l)
    diagram.get_label_by_id('010').set_text(total_b)
    diagram.get_label_by_id('001').set_text(total_m)
    diagram.get_label_by_id('110').set_text(total_l_b)
    diagram.get_label_by_id('011').set_text(total_b_m)
    diagram.get_label_by_id('101').set_text(total_l_m)
    diagram.get_label_by_id('111').set_text(total_l_b_m)

    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

    plt.text(-0.90, 0.67,
            f"Universo = {universal}",
            size=10)

    plt.text(0.30, -0.65,
            f"Fuera del conjunto = {fuera_del_conjunto}",
            size=10)

    plt.text(-1.10, -0.40,
            s=f"biologia, matematica y literatura = {total_l_b_m}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.50,
            s=f"literatura y matematica = {total_l_m}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))
                    
    plt.text(-1.10, -0.60,
            s=f"literatura = {total_l}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.70,
            s=f"biologia= {total_b}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.80,
            s=f"matematica= {total_m}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.90,
            s=f"aprobaron 2 de 3 examenes= {total_dos_de_tres}",
            size=8,
            ha="left",
            va="bottom",
            bbox=dict(boxstyle="square",
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.axis('on')
    plt.title("Parcial Matematica III")
    plt.show()


if __name__ == '__main__':
    main()
