"""
3. El plano muestra los puntos de conexión y las posibles líneas telefónicas en una urbanización. La zona quedará comunicada cuando dos puntos cualesquiera estén conectados. En rojo está indicado el precio de cada línea en miles de dólares. Calcular el diseño de la red más barata que conecte la zona.

Construir el grafo y calcular: Radio, diámetro, excentricidad, centro, periferia y densidad.
"""

from cProfile import label
import networkx as nx
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

def main():
    
    # Creo el grafo
    G = nx.Graph()

    # Creo sus nodos
    nodos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

    #Agrego los nodos al grago
    G.add_nodes_from(nodos)

    # Enlazo los nodos
    G.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'c'), ('c', 'e'), ('c', 'f'), ('c', 'd'), ('d', 'f'), ('d', 'g'), ('e', 'h'), ('e', 'i'), ('e', 'f'), ('f', 'i'), ('f', 'g'), ('g', 'j'), ('h', 'k'), ('h', 'l'), ('h', 'i'), ('i', 'l'), ('i', 'j'), ('j', 'l'), ('j', 'm'), ('k', 'n'), ('k', 'l'), ('l', 'n'), ('l', 'm'), ('m', 'n')])

    # Configuro los pesos de las aristas
    G.add_weighted_edges_from([('a', 'b', 6), ('a', 'c', 9), ('a', 'd', 3), ('b', 'e', 12), ('b', 'c', 10), ('c', 'e', 3), ('c', 'f', 2), ('c', 'd', 4), ('d', 'f', 15), ('d', 'g', 10), ('e', 'h', 4), ('e', 'i', 11), ('e', 'f', 8), ('f', 'i', 10), ('f', 'g', 9), ('g', 'j',13), ('h', 'k',20), ('h', 'l',11), ('h', 'i',7), ('i', 'l',11), ('i', 'j',15), ('j', 'l',11), ('j', 'm',9), ('k', 'n',6), ('k', 'l',13), ('l', 'n',12), ('l', 'm',5), ('m', 'n',5)])

    labels = nx.get_edge_attributes(G, 'weight') #Peso de los enlaces

    #posiciones del nodo
    pos = {'a':(0,5), 'b':(5,10), 'c':(5,5), 'd':(5,0), 'e':(10,10), 'f':(10,5), 'g':(10,0), 'h':(15,10), 'i':(15,5), 'j':(15,0), 'k':(20,10), 'l':(20,5), 'm':(20,0), 'n':(25,5)}

    #dibujo los nodos
    nx.draw_networkx(G, pos=pos, label=nodos)

    #dibujo las aristas
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='red' ,edge_labels=labels)

    #Calculos
    #Imprimo el radio
    print(f"Radio: {nx.radius(G)}\n")

    #Imprimo  el diametro
    print(f'Diametro: {nx.diameter(G)}\n')

    #Imprimo la excentricidad
    print(f'Excentricidad: {nx.eccentricity(G)}\n')

    #Imprimo el centro
    print(f'Centro: {nx.center(G)}\n')

    #Imprimo la periferia
    print(f'Periferia: {nx.periphery(G)}\n')

    #Imprimo la densidad
    print(f'Densidad: {nx.density(G)}\n')

    plt.title('Ejercicio 3')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
