"""
4. Sea G = (V,A) el grafo ponderado de 8 vértices, los cuales etiquetamos de A a H que representan poblaciones entre las cuales se implementará un medio de transporte. Los valores representan cantidad de combustible a utilizar.
Determinar qué cantidad de combustible se necesitará utilizar en una ruta que conecte las poblaciones A y H, corresponde con el problema de encontrar el camino más corto de A a H.
"""

import networkx as nx
import matplotlib.pyplot as plt

def main():

    #Creo grafo
    G = nx.Graph()

    #Creo el array de nodos y aristas
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edges = [('A','B'), ('A','E'), ('E','F'), ('F','D'), ('B','C'), ('F','G'), ('F','H')]

    #Agrego los nodos al grafo
    G.add_nodes_from(nodos)

    #Enlazo los nodos del grafo
    G.add_edges_from(edges)

    #Dibujo los nodos
    nx.draw_networkx(G)

    #Hago configuraciones de las aristas
    

    #Pinto el grafico
    plt.title('Ejercicio 4')
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    main()
