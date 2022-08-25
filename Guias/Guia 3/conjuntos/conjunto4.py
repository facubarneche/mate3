"""
4. Diseña un programa que facilite el trabajo con conjuntos. Recuerda que un conjunto es una lista en la que no hay elementos repetidos. Debes implementar:
• lista_a_conjunto(lista): Devuelve un conjunto con los mismos elementos que hay en lista, pero sin repeticiones.
(Ejemplo: lista_a_conjunto([1,1,3,2,3]) devolverá la lista [1, 2, 3] (aunque también se acepta como equivalente cualquier permutación de esos mismos elementos, como [3,1,2] o [3,2,1]).
• union(A, B): devuelve el conjunto resultante de unir los conjuntos A y B.
• interseccion(A, B): devuelve el conjunto cuyos elementos pertenecen a A y a B.
• diferencia(A, B): devuelve el conjunto de elementos que pertenecen a A y no a B.
• iguales(A, B): devuelve cierto si ambos conjuntos tienen los mismos elementos, y falso en caso contrario.
"""

def main():

    array = [1, 1, 3, 2, 3]
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    #Pasa un array a un conjunto
    def list_to_set(array):
        new_set = set(array)
        print(new_set)

    #Devuelve la union de 2 conjuntos
    def union(set1, set2):
        new_set = set1 | set2
        print(new_set)

    #Devuelve la interseccion de 2 conjuntos
    def intersection(set1, set2):
        new_set = set1 & set2
        print(new_set)

    #Devuelve un conjunto de numeros que solo pertenecen al conjunto 1
    def difference(set1, set2):
        new_set = set1 - set2
        print(new_set)

    #Devuelve si es igual o no
    def equal(set1, set2):
        
        if set1 == set2:
            new_set = True
        else:
            new_set = False

        print(new_set)  

    list_to_set(array)
    union(set1, set2)
    intersection(set1, set2)
    difference(set1, set2)
    equal(set1, set2)

if __name__ == '__main__':
    main()
