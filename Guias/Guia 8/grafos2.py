#2 . Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud mínima entre los vértices Z y A. Construir el grafo.

from cProfile import label
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def main():
    
    #Crea un Grafo
    G = nx.Graph()

    #nodos
    nodos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Agrega nodos
    G.add_nodes_from(nodos)

    # Enlaza los nodos desde una lista de tuplas, Aristas 
    G.add_edges_from([('a','b'),('b','c'),('c', 'm'), ('m', 'z'), ('a', 'j'), ('c', 'h'), ('h', 'e'), ('z', 'a'), ('p', 'o'), ('x', 'h'), ('x', 'y'), ('a', 'r'), ('r', 'l'), ('l', 's'), ('l', 'a'), ('x', 'a'), ('a', 'y'), ('y', 'b'), ('c', 'v'), ('v', 'h'), ('v', 'e'), ('a', 'q'), ('e', 'i'), ('i', 'o'), ('o', 'u'), ('u', 'a'), ('z', 'w'), ('w', 'h'), ])

    #Posiciones randoms para los nodos
    pos = nx.random_layout(G)

    # Se dibuja los nodos con sus configuraciones
    nx.draw_networkx(G, pos=pos, label=nodos, arrows=True, node_size=800,
    edgecolors = "gray")

    # Algoritmo de Dijkstra
    print("Ruta mas corta usando el algoritmo de Dijkstra entre a y e:\n", nx.algorithms.dijkstra_path(G,'a','e'))

    plt.rcParams["figure.figsize"]=[7,7]
    plt.rcParams["figure.autolayout"] = True
    plt.title("Ejercicio 2")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
