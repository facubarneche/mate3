# Ejercicio 1
""" (valor = 3 puntos)
Dada la siguiente matriz que determina nodos, pesos y conexiones, resolver usando networkx: 

   a  b  c  d  e  t
a    12    14
b        7  4  11 23
c               2 10
d               6
e                  9

a) Construir los nodos                  
b) Construir con enlaces y pesos        
c) Emitir números de nodos              
d) Emitir los nodos                     
e) Emitir números de enlaces            
f) Emitir los enlaces                   
g) Emitir los vecinos de "b"            
h) Emitir cantidad de aristas de cada nodo  
i) Convertir en diccionario la salida anterior  
j) Crear la matriz de adyacencia y emitirla     
k) Crear la matriz de incidencia y emitirla
l) Emitir valores de los enlaces del nodo "c"
m) Emitir el peso de la relación entre "b" y "e"
n) Emitir la ruta más corta desde "a" al objetivo
o) Emitir la longitud desde "a" hasta el objetivo
p) Emitir el promedio de la ruta más corta usando el método de floyd-warshall
q) Emitir la ruta ponderada más corta entre "a" y "t" usando el algoritmo de Dijkstra
r) Emitir la longitud de la ruta ponderada entre "a" y "t"
s) Emitir la longitud de la ruta desde el nodo "c"
t) Emitir el radio del grafo
u) Emitir el diámetro del grafo
v) Emitir la excentricidad
w) Emitir el centro del grafo
x) Emitir la periferia del grafo
y) Emitir la densidad.
z) Dibujar el grafo y emitir con matplotlib.pyplot
aa) Convertir en grafo dirigido. Dibujar el nuevo grafo y emitir con matplotlib.pyplot

# Ejercicio 2
(valor = 3 puntos)
Las siguientes líneas de texto fueron extraídas de un archivo con muchas entradas,
representan: ip, usuario, fecha y hora y petición. Encuentra la expresión regular
para extraer y emitir la cadena entre "". Desarrolla el código correspondiente. 

98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180 

#  Ejercicio 3
(valor = 2 puntos)
Crear la clase grafo con sus métodos (en Python) para el ejercicio 1.

# Ejercicio 4
(valor = 2 puntos)
Crear la clase regex con sus métodos (en Python) para el el ejercicio 2. 
"""

from cProfile import label
import networkx as nx
import matplotlib.pyplot as plt
import re

class Grafo:
   def __init__(self):
      self.G = nx.Graph()

   def agregarAlGrafo(self, nodos, edges, weight):
      self.G.add_nodes_from(nodos)
      self.G.add_edges_from(edges)
      self.G.add_weighted_edges_from(weight)

   def dibujarGrafo(self):
      pos = nx.shell_layout(self.G)
      labelss = nx.get_edge_attributes(self.G, 'weight')
      nx.draw_networkx(self.G,pos=pos)
      nx.draw_networkx_nodes(self.G,pos=pos,node_size=800, node_color='blue')
      nx.draw_networkx_edges(self.G, pos=pos)
      nx.draw_networkx_edge_labels(self.G,pos=pos, edge_labels=labelss)
      nx.draw_networkx_labels(self.G,pos=pos)

   def contestarConsignas(self):     
      #c) Emitir números de nodos   
      print(f'Números de nodos: {self.G.number_of_nodes()}')           
      #d) Emitir los nodos     
      print(f'Nodos: {self.G.nodes()}')                  
      #e) Emitir números de enlaces   
      print(f'Enlaces: {self.G.number_of_edges()}')           
      #f) Emitir los enlaces          
      print(f'Enlaces: {self.G.edges()}')         
      #g) Emitir los vecinos de "b"   
      print(f'Vecinos de "b": {list(nx.neighbors(self.G, "b"))}')         
      #h) Emitir cantidad de aristas de cada nodo  
      print(f'Cantidad de aristas de cada nodo: {nx.degree(self.G)}')      
      #i) Convertir en diccionario la salida anterior
      print(f'Cantidad de aristas de cada nodo como diccionario: {dict(nx.degree(self.G))}')        
      #j) Crear la matriz de adyacencia y emitirla
      A = nx.adjacency_matrix(self.G)
      print(f'Matriz de adyacencia:\n{A.todense()}')
      #k) Crear la matriz de incidencia y emitirla
      I = nx.incidence_matrix(self.G)
      print(f'Matriz de incidencia:\n{I.todense()}')
      #l) Emitir valores de los enlaces del nodo "c"
      print(f'Valores de los enlaces del nodo "c": {self.G["c"]}')    
      #m) Emitir el peso de la relación entre "b" y "e"
      print(f'Peso de la relacion entre b y c: {self.G["c"]["b"]["weight"]}')
      #n) Emitir la ruta más corta desde "a" al objetivo
      print(f'Ruta mas corta desde a al objetivo: {nx.algorithms.single_source_shortest_path(self.G, "a")}')
      #o) Emitir la longitud desde "a" hasta el objetivo
      print(f'Long desde a hasta objetivo: {nx.single_source_shortest_path_length(self.G, "a")}')
      #p) Emitir el promedio de la ruta más corta usando el método de floyd-warshall
      print(f'Promedio ruta mas corta con floyd-warshall: {nx.average_shortest_path_length(self.G, method="floyd-warshall")}')
      #q) Emitir la ruta ponderada más corta entre "a" y "t" usando el algoritmo de Dijkstra
      print(f':ruta ponderada mas corta entre a y t con dijkstra {nx.dijkstra_path(self.G, "a", "t")}')
      #r) Emitir la longitud de la ruta ponderada entre "a" y "t"
      print(f'Long entre a y t ponderada: {nx.dijkstra_path_length(self.G, "a", "t")}')
      #s) Emitir la longitud de la ruta desde el nodo "c"
      print(f'Long de la ruta desde el nodo c: {nx.single_source_dijkstra_path_length(self.G,"c")}')
      #t) Emitir el radio del grafo
      print(f'radio: {nx.radius(self.G)}')
      #u) Emitir el diámetro del grafo
      print(f'diametro: {nx.diameter(self.G)}')
      #v) Emitir la excentricidad
      print(f'excentricidad: {nx.eccentricity(self.G)}')
      #w) Emitir el centro del grafo
      print(f'centro: {nx.center(self.G)}')
      #x) Emitir la periferia del grafo
      print(f'periferia: {nx.periphery(self.G)}')
      #y) Emitir la densidad.
      print(f'densidad: {nx.density(self.G)}')      
      
   def mostrarGrafo(self, title):
      plt.title(title)
      plt.axis('off')
      plt.show()

   def redirigirGrafo(self):
      return self.G.to_directed()



nodos = ['a','b','c','d','e','t']
edges = [('a','b'),('a','d'),('b','c'),('b','d'),('b','e'),('b','t'),('c','e'),('c','t'),('d','e'),('e','t')]
weight_edges = [('a','b',12),('a','d',14),('b','c',7),('b','d',4),('b','e',11),('b','t',23),('c','e',2),('c','t',10),('d','e',6),('e','t',9)]

grafo = Grafo()
grafo.agregarAlGrafo(nodos, edges, weight_edges)
grafo.dibujarGrafo()
grafo.contestarConsignas()
grafo.mostrarGrafo('Segundo Parcial Matemática III')

