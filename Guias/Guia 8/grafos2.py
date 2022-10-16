#2 . Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud mínima entre los vértices Z y A. Construir el grafo.

from cProfile import label
import networkx as nx
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

def main():
    
    #Crea un Grafo
    G = nx.Graph()

    #nodos
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z']
    
    # Agrega nodos
    G.add_nodes_from(nodos)

    # Enlaza los nodos desde una lista de tuplas, Aristas 
    G.add_edges_from([('A','B'), ('A','D'), ('A','G'), ('D','G'), ('B','G'), ('Z','F'), ('Z','E'), ('Z','C'), ('E','F'), ('C','F'), ('D','E'), ('B','C')])

    G.add_weighted_edges_from([('A','B', 4), ('A','D', 5), ('A','G', 2), ('D','G', 1), ('B','G', 1), ('Z','F', 2), ('Z','E', 3), ('Z','C', 1), ('E','F', 1), ('C','F', 1), ('D','E', 2), ('B','C', 5)])

    labels = nx.get_edge_attributes(G, 'weight') # pesos de los enlaces

    #Posiciones randoms para los nodos (no sirve para este ejercicio pero lo guardo)
    #pos = nx.random_layout(G)

    pos = {'A':(30, 5), 'B':(22.5, 0), 'C':(7.5, 0), 'D':(22.5, 10), 'E':(7.5, 10), 'F':(7.5, 5), 'G':(22.5, 5), 'Z':(0, 5)}

    # Se dibuja los nodos con sus configuraciones
    nx.draw_networkx(G, pos=pos, label=nodos, node_size=800,
    edgecolors = "blue")

    # (grafo, posicion, etiquietas aristas, color aristas)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_color='black')

    # Algoritmo de Dijkstra
    print("Ruta mas corta usando el algoritmo de Dijkstra entre a y e:\n", nx.algorithms.dijkstra_path(G,'A','E'))

    plt.title("Ejercicio 2")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
