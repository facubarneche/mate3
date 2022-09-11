"""
1. Dado el siguiente problema con su programación en Python. Genera los gráficos con Diagramas de Venn que representen las respuestas de los encuestados. Investiga si puedes utilizar subplots para representar todas las operaciones:
Un grupo de jóvenes fue entrevistado para conocer sus preferencias de los siguientes medios de transporte: moto, auto y bicicleta. Los datos de la encuesta fueron los siguientes:
- 5 jóvenes prefieren solamente la moto -OK-
- 38 jóvenes prefieren la moto -OK-
- A 9 jóvenes no les gusta el automóvil como medio de transporte -OK-
- 3 jóvenes prefieren la moto y la bicicleta, pero no el auto -OK-
- 20 prefieren la moto y el auto, pero no la bicicleta -OK-
- A 72 no les gusta la bicicleta como medio de transporte 
- Un solo joven, no prefiere ninguno de estos tres medios de transporte
- A 61 no les gusta la moto como medio de transporte -OK-
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

def main():

    M={5,20,3,10}
    A={46,20,10,14}
    B={0,3,10,14}
    U={1}
    #Muestro los conjuntos
    print(f"Los conjuntos son: /n M={M}, A={A}, B={B} y U={U}\n")
    #Funcion in
    print("Funcion in. Busco si 5 esta en el conjunto M: ")
    print(5 in M, end=" \n")
    #Funcion len
    print("Funcion len. Muestro el modulo de A: ")
    print(len(A))
    #Funcion not
    print("Funcion not. Muestro si 10 no esta en B: ")
    print(10 not in B, end= "\n")
    #Funcion add
    print("Funcion add. Añado un elemento al conjunto U: ")
    print(U.add('x'), end=" \n")
    #Funcion remove
    print("Funcion remove. Elimino un elemento al conjunto U: ")
    print(U.remove('x'), end=" \n")
    #Funcion intersection
    print("Funcion intersection. Muestro la interseccion entre B y A: ")
    print(B&A, end=" \n")
    #Funcion union
    print("Funcion union. Muestro la union entre M y A: ")
    print(M|A, end=" \n")
    #Funcion diferencia -
    print("Funcion diferencia. Aplico la funcion diferencia entre A y B: ")
    print (A-B, end=" \n")
    #Funcion ^
    print("Funcion diferencia. Aplico la funcion diferencia simetrica entre A y B: ")
    print(A^B, end= " \n")
    #Funcion issubset
    print("Funcion issubset. Muestro si M es un subconjunto de A: ")
    print(M.issubset(A), end=" \n")

    def add_people(plus_set):
        total = 0
        for plus in plus_set:
            total += plus
        
        return total
    #end def

    print(f'Total de motos => {add_people(M)}')#38 motos
    print(f'Total de autos => {add_people(A)}')#90 autos
    print(f'Total de bicicletas => {add_people(B)}')#27 bicis
    print(f'Total sin preferencias => {add_people(U)}')#1 sin preferencias

    def everybody(prefer1, prefer2, prefer3):
        return prefer1 & prefer2 & prefer3

    myayb = everybody(M, A, B)
    print(f'Que hacen los 3 deportes => {myayb}')#Hacen los 3 deportes

    def only_2(prefer1, prefer2):
        return prefer1 & prefer2

    mya = only_2(M, A)
    print(mya)#Solo motos y autos
    myb = only_2(M, B)
    print(myb)#Solo motos y bicis
    ayb = only_2(A, B)
    print(ayb)#Solo autos y bicis

    def only_1(prefer1, prefer2, prefer3):
        return (prefer1 - prefer2) & (prefer1 - prefer3)

    only_m = only_1(M, A, B)
    print(only_m)#Solo andan en moto

    only_a = only_1(A, M, B)
    print(only_a)#Solo andan en auto

    only_b = only_1(B, A, M)
    print(only_b)#Solo andan en bici



##################################################################################
# Gráfico de resultados
##################################################################################
# preparamos la ventana del gráfico
    plt.figure('Ejercicio 1 conjunto')

    # dibujamos los diagramas
    diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
        "Moto", "Auto", "Bici"))

    # establecemos el tamaño de la fuente
    for subset in ("111", "110", "101", "100", "011", "010", "001"):
        diagram.get_label_by_id(subset).set_fontsize(10)

    # transferimos los resultados de las operaciones
    diagram.get_label_by_id('100').set_text(only_m)
    diagram.get_label_by_id('010').set_text(only_a)
    diagram.get_label_by_id('001').set_text(only_b)
    diagram.get_label_by_id('110').set_text(mya - myayb)
    diagram.get_label_by_id('011').set_text(ayb - myayb)
    diagram.get_label_by_id('101').set_text(myb - myayb)
    diagram.get_label_by_id('111').set_text(myayb - U)

    plt.show()

    
if __name__ == '__main__':
    main()
