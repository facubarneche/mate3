"""
1 bis) Luego, a raíz de una entrega urgente de proyecto, todos se involucran en el mismo con una carga de horas de trabajo estimada, coordinando la dirección de entrega de cada parte a otra, según una planificación:
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def main():

    #Crea un diGrafo
    G = nx.DiGraph()

    #arange genera un conjunto de números entre un valor de inicio y final, pudiendo especificar un incremento entre los valores
    #Un array de numpy se puede convertir a lista de Python utilizando tolist()
    nodos = np.arange(0, 8).tolist()

    # Agrega nodos
    G.add_nodes_from(nodos)

    # Enlaza los nodos desde una lista de tuplas, Aristas 
    G.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,7),(3,5),(7,4),(0,6),(2,3)])

    # Se ponen etiquetas a cada nodo
    labels={0:"CEO",1:"Líder\nX",2:"Líder\nY",3:"A", 4:"B",5:"C",6:"D",7:"E"}

    # Se ponen los colores para cada nodo
    colors = ["snow","turquoise","orange","turquoise","turquoise","orange","orange","orange"]

    # Se ponen los colores de cada arista
    edge_colors = ["turquoise","orange","turquoise","turquoise","orange","orange","orange"]

    # Se configuran los tamaños de cada nodo
    sizes = [1000, 2000, 2000, 1200, 1200, 1200, 1200, 1200]

    # Se dibuja los nodos con sus configuraciones
    nx.draw_networkx(G, pos=nx.shell_layout(G), labels=labels, arrows=True, #(grafo, posiciones, etiquetas y modo flecha activado)
    node_shape = "s", node_size = sizes, #forma y tamaño de nodos
    node_color = colors,        #Color de nodos
    edge_color = edge_colors,   #Color de aristas
    edgecolors = "gray", # Bordes de nodos
    font_size=8) #Tamaño fuente

    plt.rcParams["figure.figsize"]=[7,7]
    
    # (grafo, posicion, etiquietas aristas, color aristas)
    nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels={(0,1):'3.0', (0,2):'4.5', 
    (1,3):'6.0',(1,4):'8.5', (2,5):'10.5',(2,6):'7.0',(2,7):'9.5',(3,5):'1.5', (7,4):'6.0',
    (0,6):'5.0',(2,3):'6.5'}, font_color='gray')
    plt.title("Proyecto Urgente")
    plt.axis('off')
    plt.show()

    """
    Calculando la centralidad
    El grado de centralidad de un nodo es la parte del total de nodos a los que está conectado. Un nodo con un alto grado de centralidad generalmente se considera altamente activo. En G, el nodo 2 (Líder Y), tiene el grado más alto de centralidad ya que está conectado a otros cuatro nodos.
    """

    centrality = nx.degree_centrality(G)
    print(f'nx.degree_centrality (grado de centralidad) \n{centrality}')

    # Devuelve los valores de un diccionario en un array
    def valores(c):
        return list(c.values())

    val = valores(nx.degree_centrality(G))
    eti = valores(labels)

    # Grafico de barras, etiquetas, valores, ancho de barra y color
    plt.bar(np.array(eti), np.array(val), width = 0.5 ,color='lightcoral')
    plt.show()

    """
    La centralidad de intermediación es una medida de cuántas veces un nodo en particular se encuentra en el camino más corto entre todos los pares de nodos en un gráfico. En G, el líder Y tiene la centralidad de intermediación más alta, seguido del líder X. Esto implica que los líderes de equipo actúan como puentes entre el CEO y el personal. Luego le siguen A y E. El CEO tiene una centralidad de intermediación cero porque no se encuentran entre dos nodos.
    """

    between_centrality = nx.betweenness_centrality(G)
    print(f'nx.betweenness_centrality (centralidad de intermediacion) \n{between_centrality}')

    val2 = valores(nx.betweenness_centrality(G))
    plt.bar(np.array(eti), np.array(val2), width = 0.5 ,color='springgreen')
    plt.show()

    """
    La centralidad de cercanía es una medida de la proximidad de un nodo a otros nodos. Se calcula como el promedio de la longitud de la ruta más corta desde el nodo hasta todos los demás nodos de la red. En el caso de la centralidad de cercanía, los nodos con valores más bajos tienen una centralidad más alta. Esto implica que el CEO y los líderes de equipo tienen más centralidad de cercanía en comparación con el personal.
    """

    closer_centrality = nx.closeness_centrality(G)
    print(f'nx.closeness_centrality (centralidad de cercania) \n{closer_centrality}')

    val3 = valores(nx.closeness_centrality(G))
    plt.bar(np.array(eti), np.array(val3), width = 0.5 ,color='gold')
    plt.show()

if __name__ == '__main__':
    main()

