#1 Crear la clase Grafo para el ejercicio  del punto 2
#2 Dada la sig matriz que determina nodos, pesos y conexiones, resolver usando networkx
"""
    A   B   C   D   E   F   G
A               6       2
B   5               12      1
C           4
D                           2
E           6
F   9

"""
#a Construir los nodos con enlaces y pesos
#b Emitir los vecinos de 'c'
#c Crear y emitir la matriz de adyacencia e incidencia
#d Emitir la ruta ponderada mas corta entre 'd' y 'f' usando el algoritmo de Dijkstra
#e Emitir el radio, diametro, excentricidad, centro, periferia y densidad
#f Dibujar el grafo con matplotlib.pyplot

#3 Dadas las siguientes lineas de codigo
""" 
"3475","3592","Male","52","GBR","217.4833333","Regular"
"13594","13853","Female","40","NY","272.55","Regular"
"12012","12256","Male","31","FRA","265.2833333","Regular"
"10236","10457","Female","33","MI","256.15","Regular"
"9476","9686","Male","33","NY","252.25","Regular"
"1720","1784","Male","40","NJ","201.9666667","Regular"
"15736","16020","Female","30","CA","283.5666667","Regular" 
"""
# Hallar la expresión regular para extraer una lista con los nombres de ciudades ejemplo ['GBR', 'NY', 'FRA', 'MI'...]. Construye el programa en python para verificar que funcione            

#Importaciones
import networkx as nx
import matplotlib.pyplot as plt
import re

#Ejercicio 1

#Creo la clas Grafo
class Grafo:
    #Uso __init__ como constructo para obligar a crear la instancia Grafo con sus atributos
    def __init__(self):
        self.G = nx.Graph()

    def agregarAlGrafo(self, nodos, edges, weight):
        self.G.add_nodes_from(nodos)
        self.G.add_edges_from(edges)
        self.G.add_weighted_edges_from(weight)

    def dibujarGrafo(self):
        #Asigno a pos, la posicion que quiero para el grafo
        pos = nx.shell_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx(self.G, pos)
        nx.draw_networkx_nodes(self.G, pos, node_size= 800, node_color= 'skyblue')
        nx.draw_networkx_edges(self.G, pos, edge_color='blue')
        nx.draw_networkx_labels(self.G, pos, font_size=15)
        nx.draw_networkx_edge_labels(self.G, pos=pos, edge_labels=labels, font_color='blue')

    def consignasGrafo(self):
        #b Emitir los vecinos de 'c'
        print(f'\n#b Emitir los vecinos de "c": {list(self.G.neighbors("C"))}')
        #c Crear y emitir la matriz de adyacencia e incidencia
        print(f'\n#c Crear y emitir la matriz de adyacencia e incidencia: {nx.adj_matrix(self.G).todense()}')
        #d Emitir la ruta ponderada mas corta entre 'd' y 'f' usando el algoritmo de Dijkstra
        print(f'\n#d Emitir la ruta ponderada mas corta entre "d" y "f" usando el algoritmo de Dijkstra: {nx.algorithms.dijkstra_path(self.G, "D", "F")}')
        #e Emitir el radio, diametro, excentricidad, centro, periferia y densidad
        print(f'\n#e Emitir el radio, diametro, excentricidad, centro, periferia y densidad:\
        \nRadio: {nx.radius(self.G)}\
        \nDiametro : {nx.diameter(self.G)}\
        \nExcentricidad: {nx.eccentricity(self.G)}\
        \nCentro: {nx.center(self.G)}\
        \nPeriferia: {nx.periphery(self.G)}\
        \nDensidad: {nx.density(self.G)}')
        
    def mostrarGrafo(self, title):
        plt.title(title)
        plt.axis('off')
        plt.show()
    
#Ejercicio 2

#Se crean las variables con los nodos, enlaces y pesos de enlaces
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [('A','D'),('A','F'),('B','A'),('B','E'),('B','G'),('C','C'),('D','G'),('E','C'),('F','A')]
edges_weight = [('A','D',6),('A','F',2),('B','A',5),('B','E',12),('B','G',1),('C','C',4),('D','G',2),('E','C',6),('F','A',9)]

#Creo una instancia de la clase Grafo y le asigno los nodos, enlaces y pesos de enlaces para luego agregarlos al grafo
G = Grafo()

#Agrego al grafo los atributos
G.agregarAlGrafo(nodos, edges, edges_weight)

#Dibujo el grafo
G.dibujarGrafo()

#Respuesta de las consignas
G.consignasGrafo()

#f Dibujar el grafo con matplotlib.pyplot
G.mostrarGrafo('Segundo Parcial Matemática III')

#Ejercicio 3

#Texto a filtrar
texto =""" 
"3475","3592","Male","52","GBR","217.4833333","Regular"
"13594","13853","Female","40","NY","272.55","Regular"
"12012","12256","Male","31","FRA","265.2833333","Regular"
"10236","10457","Female","33","MI","256.15","Regular"
"9476","9686","Male","33","NY","252.25","Regular"
"1720","1784","Male","40","NJ","201.9666667","Regular"
"15736","16020","Female","30","CA","283.5666667","Regular" 
"""

#Regex para que filtro lo buscado en este caso 'GBR', 'NY' ...
regex = '[A-Z]{2,3}'
#Le asigno a una variable el texto filtrado
texto_filtrado = re.findall(regex, texto)
#Imprimo el texto filtrado
print(texto_filtrado)