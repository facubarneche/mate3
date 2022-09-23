from ast import Dict
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
    
    ##################################################################################
    # Declaraciones y analisis de primeros datos
    ##################################################################################

    universal = 1000    #Universo de 1000 alumnos
    ninguno = 0

    #Literatura => Diccionario, aprobaron 680
    literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
    "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}

    #Biologia => Tupla, aprobaron 320
    biologia = (40, 50, 60, 75, 34, 61)

    #Matematica => lista, aprobaron 490
    matematica = [34, 40, 61, 75, 87, 90, 103]


    ##################################################################################
    # Comprobación de datos
    ##################################################################################

    def addition(subject):
        if type(subject) == dict:
            return sum(subject.values())
        else:
            return sum(subject)
    #FinDef

    #Comprobamos que los datos recibidos son correctos
    print('')
    print('Comprobamos que los datos recibidos son correctos', end="\n\n")
    print(f'La suma de literatura debe ser 680 para ser correcto = {addition(literatura)}')
    print(f'La suma de biologia debe ser 320 para ser correcto = {addition(biologia)}')
    print(f'La suma de matematica debe ser 490 para ser correcto = {addition(matematica)}', end="\n\n")

    ##################################################################################
    # Convertimos los datos recibidos a Set
    ##################################################################################

    def setter(subject):
        if type(subject) == dict:
            return set(subject.values())
        else:
            return set(subject)
    #FinDef

    #Asignamos las nuevas variables, los datos recibidos en tipo set 
    setLiteratura   = setter(literatura)
    setBiologia     = setter(biologia)
    setMatematica   = setter(matematica)

    #Comprobamos que son tipo set y que tienen el mismo valor que los datos recibidos anteriormente 
    print('Comprobamos que son tipo set y que tienen el mismo valor que los datos recibidos anteriormente', end="\n\n")
    print(f'setLiteratura es del tipo {type(setLiteratura)} y su valor es {setLiteratura}')
    print(f'setBiologia es del tipo {type(setBiologia)} y su valor es {setBiologia}')
    print(f'setMatematica es del tipo {type(setMatematica)} y su valor es {setMatematica}', end='\n\n')

    ##################################################################################
    # Calculos y funciones para resolver el enunciado
    ##################################################################################

    #Calcula la intersección de las 3 materias
    def lite_bio_mate(subj1, subj2, subj3):
        return subj1 & subj2 & subj3

    #Calcula la intersección entre 2 materias (excluyendo la triple intersección)
    def inter2(subj1, subj2):
        return ( subj1 & subj2 ) - l_b_m

    #Calculo los estudiantes de 1 solo materia
    def just1(subj1, subj2, subj3):
        return subj1 - subj2 - subj3

    #Asigno nuevas variables con los calculos hechos, pasandole como parametro las variables seteadas
    l_b_m = lite_bio_mate(setLiteratura, setBiologia, setMatematica)    #Triple intersección

    #Asigno nuevas variables para las intersecciones de literatura y biologia, literatura y matematica y biologia y matematica
    l_b = inter2(setLiteratura, setBiologia)
    l_m = inter2(setLiteratura, setMatematica)
    b_m = inter2(setBiologia, setMatematica)

    #Asigno nueva variables para los alumnos que solo estudian 1 materia
    l = just1(setLiteratura, setBiologia, setMatematica)
    b = just1(setBiologia, setLiteratura, setMatematica)
    m = just1(setMatematica, setLiteratura, setBiologia)

    #Hago un print de las variables recien asignadas
    print('Hago un print de las variables recien asignadas', end ='\n\n')
    print(f'Aprobaron literatura, matematica y biologia {l_b_m} alumnos')
    print(f'Aprobaron literatura y matematica {l_m} alumnos')
    print(f'Aprobaron literatura y biologia {l_b} alumnos')
    print(f'Aprobaron biologia y matematica {b_m} alumnos')
    print(f'Aprobaron literatura {l} alumnos')
    print(f'Aprobaron biologia {b} alumnos')
    print(f'Aprobaron matematica {m} alumnos', end="\n\n")

    ##################################################################################
    # Realizo la suma del conjunto para devolverlo como valor unico
    ##################################################################################

    #Sumo los conjuntos y devuelvo un unico valor
    def setAddition(setParam):
        return sum(setParam)

    #Asigno en variables el valor total de alumnos que estudian el requisito correspondiente
    addLite = setAddition(l)
    addBio = setAddition(b)
    addMate = setAddition(m)
    addLite_bio = setAddition(l_b)
    addLite_mate = setAddition(l_m)
    addBio_mate = setAddition(b_m)
    addLite_bio_mate = setAddition(l_b_m)

    #Imprimimos los valores por consola de la suma de las variables recientemente realizadas
    print('Imprimimos los valores por consola de la suma de las variables recientemente realizadas', end="\n\n")
    print(f'Los alumnos que estudian literatura son {addLite} alumnos')
    print(f'Los alumnos que estudian biologia son {addBio} alumnos')
    print(f'Los alumnos que estudian matematica son {addMate} alumnos')
    print(f'Los alumnos que estudian literatura y biologia son {addLite_bio} alumnos')
    print(f'Los alumnos que estudian literatura y matematica son {addLite_mate} alumnos')
    print(f'Los alumnos que estudian biologia y matematica son {addBio_mate} alumnos')
    print(f'Los alumnos que estudian literatura, biologia y matematica son {addLite_bio_mate} alumnos', end="\n\n")

    ##################################################################################
    # Respuesta a las preguntas
    ##################################################################################

    """
    a. cuántos aprobaron biología matemática y literatura.
    b. cuántos aprobaron sólo literatura y matemática?
    c. cuántos aprobaron sólo literatura?
    d. cuántos aprobaron solo biología?
    e. cuántos aprobaron sólo matemática?
    """

    #Funciones para resolver la pregunta 3
    def questionE(inter1, inter2, inter3):
        return sum(((inter1 & inter2) | (inter1 & inter3) | (inter2 & inter3)) - l_b_m)
    #FinDef

    #Asigno variable a la pregunta e
    qE = questionE(setLiteratura, setBiologia, setMatematica)

    print('Respuesta a las preguntas')
    print(f'Aprobaron biologia, matematica y literatura {addLite_bio_mate} alumnos')
    print(f'Aprobaron solo literatura y matematica {addLite_mate} alumnos')
    print(f'Aprobaron solo literatura {addLite} alumnos')
    print(f'Aprobaron solo biología {addBio} alumnos')
    print(f'Aprobaron solo matemática {addMate} alumnos')
    print(f'Aprobaron 2 de los 3 examenes {qE} alumnos')


    ##################################################################################
    # Gráfico de resultados
    ##################################################################################

    # preparamos la ventana del gráfico
    plt.figure('Ejemplo de primer parcial ')
    
    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
        "Literatura", "Biologia", "Matematica"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(10)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text(addLite)
    diagram.get_label_by_id('010').set_text(addBio)
    diagram.get_label_by_id('001').set_text(addMate)
    diagram.get_label_by_id('110').set_text(addLite_bio)
    diagram.get_label_by_id('011').set_text(addBio_mate)
    diagram.get_label_by_id('101').set_text(addLite_mate)
    diagram.get_label_by_id('111').set_text(addLite_bio_mate)

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
            s="biologia, matematica y literatura = " + str(addLite_bio_mate),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.40,
            s="literatura y matematica = " + str(addLite_mate),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.50,
            s="literatura = " + str(addLite),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.60,
            s="biologia = " + str(addBio),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.70,
            s="matematica = " + str(addMate),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.text(-1.10, -0.80,
            s="Aprobaron 2 de los 3 examenes = " + str(qE),
            size=8,
            ha="left",  # alineación horizontal
            va="bottom",  # alineación vertical
            bbox=dict(boxstyle="square",  # tipo de cuadro
                    ec=(1.0, 0.7, 0.5),
                    fc=(1.0, 0.9, 0.8),))

    plt.axis('on')  # Recuadro
    plt.title("Materias")
    plt.show()
    ##################################################################################
    # Fin de programa
    ##################################################################################


if __name__ == '__main__':
    main()
