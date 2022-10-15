"""
1. Supongamos un organigrama que muestra la estructura jerárquica de una organización y las relaciones entre los
empleados en los diferentes niveles y/o áreas dentro de ella. Consideremos que la empresa tiene 2 equipos X e Y
trabajando dentro de ella. En total hay ocho empleados en la empresa: un CEO, 2 líderes de equipo, 2 empleados en
el equipo X y 3 empleados en el equipo Y. Si cada nodo tuviera como máximo 2 nodos secundarios, habría sido un
árbol binario, en este caso en ternario. Construimos el organigrama:
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
    G.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,7)])

    # Posiciona los nodos en el grafico
    pos={ 0:(11.5,10), 1:(7.5,7.5), 2:(15,7.5),3:(6,6), 4:(9,6), 5:(12,6), 6:(15,6), 7:(18,6) }

    # Se ponen etiquetas a cada nodo
    labels={0:"CEO",1:"Líder\nX",2:"Líder\nY",3:"A", 4:"B",5:"C",6:"D",7:"E"}

    # Se ponen los colores para cada nodo
    colors = ["snow","turquoise","orange","turquoise","turquoise","orange","orange","orange"]

    # Se ponen los colores de cada arista
    edge_colors = ["turquoise","orange","turquoise","turquoise","orange","orange","orange"]

    # Se configuran los tamaños de cada nodo
    sizes = [1000, 2000, 2000, 1200, 1200, 1200, 1200, 1200]

    # Se dibuja los nodos con sus configuraciones
    nx.draw_networkx(G, pos=pos, labels=labels, arrows=True, #(grafo, posiciones, etiquetas y modo flecha activado)
    node_shape = "s", node_size = sizes, #forma y tamaño de nodos
    node_color = colors,        #Color de nodos
    edge_color = edge_colors,   #Color de aristas
    edgecolors = "gray", # Bordes de nodos
    font_size=8) #Tamaño fuente

    plt.rcParams["figure.figsize"]=[7,7]
    
    # (grafo, posicion, etiquietas aristas, color aristas)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={(0,1):'X', (0,2):'Y'}, font_color='gray')
    plt.title("La empresa")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
