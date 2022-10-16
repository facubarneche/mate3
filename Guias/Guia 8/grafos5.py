#5. Se considera el grafo ponderado G definido por la siguiente tabla, donde los vértices representan ciudades y las aristas representan rutas existentes entre las poblaciones. Los pesos indican longitudes en Kms.

from typing import Any
import networkx as nx
import matplotlib.pyplot as plt

def main():

    #Creo grafo
    G = nx.Graph()

    #Creo el array de nodos y aristas
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    
    #Agrego los nodos al grafo
    G.add_nodes_from(nodos)

    #Enlazo los nodos del grafo
    G.add_edges_from([('A','B'), ('A','F'), ('A','I'), ('B','C'), ('B','F'), ('B','I'), ('C','D'), ('C','I'), ('D','G'), ('D','H'), ('D','I'), ('E','F'), ('E','G'), ('E','H'), ('F','G'), ('F','I'), ('G','H'), ('G','I'), ('H','I')])

    #Configuro los pesos
    G.add_weighted_edges_from([('A','B',20), ('A','F',34), ('A','I',45), ('B','C',20), ('B','F',10), ('B','I',26), ('C','D',28), ('C','I',22), ('D','G',18), ('D','H',19), ('D','I',13), ('E','F',22), ('E','G',12), ('E','H',25), ('F','G',30), ('F','I',12), ('G','H',16), ('G','I',14), ('H','I',32)])

    #Posiciones
    pos = nx.random_layout(G)
    
    #Labels pesos
    labels = nx.get_edge_attributes(G, 'weight')

    #Dibujo los nodos
    nx.draw_networkx(G, pos)

    #Hago configuraciones de las aristas
    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=labels)
    

    #a. Usando el algoritmo apropiado, calcular la distancia más cortas desde A a las restantes poblaciones y especificar cuáles son dichas distancias.

    # Funcion del Algoritmo de Dijkstra
    def dijkstra(G, node1, node2):
        dist = 0
        distance = nx.algorithms.dijkstra_path(G,node1,node2)
        print (f'Distancia mas corta con el algoritmo de Dijkstra de {node1} a {node2} => {distance} y su distancia es:')

    
    def shorter(G, node1, node2):
        print (f'Distancia mas corta de {node1} a {node2} => {nx.algorithms.dijkstra_path(G,node1,node2)}')    

    dijkstra(G, 'A', 'B')
    dijkstra(G, 'A', 'C')
    dijkstra(G, 'A', 'D')
    dijkstra(G, 'A', 'E')
    dijkstra(G, 'A', 'F')
    dijkstra(G, 'A', 'G')
    dijkstra(G, 'A', 'H')
    dijkstra(G, 'A', 'I')
    print('============================')
    shorter(G, 'A', 'B')
    shorter(G, 'A', 'C')
    shorter(G, 'A', 'D')
    shorter(G, 'A', 'E')
    shorter(G, 'A', 'F')
    shorter(G, 'A', 'G')
    shorter(G, 'A', 'H')
    shorter(G, 'A', 'I')

    print(G.adj.items())
    #b. Se ha construido una nueva ruta entre las poblaciones B y G de forma que ahora, la distancia entre A y H es de 68 Kms. Determinar cuál es el peso que le corresponde a la arista {B,G}.
    


    #Pinto el grafico
    plt.title('Ejercicio 5')
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    main()
