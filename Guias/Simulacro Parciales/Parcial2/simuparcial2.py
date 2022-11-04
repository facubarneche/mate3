# Ejercicio 1
""" (valor = 3 puntos)
Dada la siguiente matriz que determina nodos, pesos y conexiones, resolver usando networkx: 

   a  b  c  d  e  t
a    12    14
b        7  4  11 23
c               2 10
d               6
e                  9

a) Construir los nodos                  -ok-
b) Construir con enlaces y pesos        -ok-
c) Emitir números de nodos              -ok-
d) Emitir los nodos                     -ok-
e) Emitir números de enlaces            -ok-
f) Emitir los enlaces                   -ok-
g) Emitir los vecinos de "b"            -ok-
h) Emitir cantidad de aristas de cada nodo  -ok-
i) Convertir en diccionario la salida anterior  -ok-
j) Crear la matriz de adyacencia y emitirla     -ok-
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

import networkx as nx
import matplotlib.pyplot as plt
import re 

def main():
    # Ejercicio 1
    G = nx.Graph()

    nodos = ['a', 'b', 'c', 'd', 'e', 't']
    edges = [('a','b'),('a','d'),('b','c'),('b','d'),('b','e'),('b','t'),('c','e'),('c','t'),('d','e'),('e','t')]
    weigthed_edges = [('a','b',12),('a','d',14),('b','c',7),('b','d',4),('b','e',11),('b','t',23),('c','e',2),('c','t',10),('d','e',6),('e','t',9)]

    def addGraph(G, nodos, edges, weigthed):
        G.add_nodes_from(nodos)#Agrega nodos al grafo
        G.add_edges_from(edges)#Agrega las enlaces
        G.add_weighted_edges_from(weigthed)#Agrega los pesos

    #Funcion para agregar nodos, enlaces y pesos y hacer sus configuraciones, quedan disponibles para luego mostrarlas (ej a y b)
    def confGraph(G):
        labels = nx.get_edge_attributes(G, 'weight')#Asigna a una variable etiqueta todos los pesos
        pos = nx.shell_layout(G)#Configura la posiciones de los nodos 
        #Dibuja el grafo con sus respectivas configuraciones de nodos, aristas y etiquetas
        nx.draw_networkx(G, pos)
        nx.draw_networkx_nodes(G, pos, node_size=600, node_color='skyblue', node_shape='h')
        nx.draw_networkx_edges(G, pos, edge_color='pink')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='blue')

    def emitirGraph(title):
        plt.title(title)
        plt.axis('off')
        plt.show()

    #Agrega los componentes del grafo
    addGraph(G, nodos, edges, weigthed_edges)
    #Utiliza la funcion para agregar nodos, enlaces, pesos y sus respectivas configuraciones    
    confGraph(G)

    print(f'c) Emitir n° nodos: {G.number_of_nodes()}')
    print(f'd) Emitir nodos: {G.nodes()}')
    print(f'e) Emitir números de enlaces: {G.number_of_edges()}')
    print(f'f) Emitir los enlaces: {dict(G.edges())}')
    print(f'g) Emitir los vecinos de "b": {list(G.neighbors("b"))}')
    print(f'h) Emitir cantidad de aristas de cada nodo: {G.degree()}')
    print(f'i) Convertir en diccionario la salida anterior: {dict(G.degree())}')
    print('j) Crear la matriz de adyacencia y emitirla: \n')

    #Creo la matriz de adyacencia
    M = nx.adjacency_matrix(G)
    print(M.todense())

    print('j) Crear la matriz de indicencia y emitirla: \n')
    
    #Creo la matriz de incidencia
    I = nx.incidence_matrix(G)
    print(I.todense())

    print(f'l) Emitir valores de los enlaces del nodo "c": {G["c"]}')
    print(f'm) Emitir el peso de la relación entre "b" y "e":  {G["b"]["e"]["weight"]}')
    print(f'n) Emitir la ruta más corta desde "a" al objetivo: {nx.algorithms.shortest_path(G,"a")}')
    print(f'o) Emitir la longitud desde "a" hasta el objetivo: {nx.single_source_shortest_path_length(G, "a")}')
    print(f'p) Emitir el promedio de la ruta más corta usando el método de floyd-warshall: {nx.average_shortest_path_length(G, method="floyd-warshall")}')
    print(f'q) Emitir la ruta ponderada más corta entre "a" y "t" usando el algoritmo de Dijkstra: {nx.algorithms.dijkstra_path(G, "a", "t")}')
    print(f's) Emitir la longitud de la ruta desde el nodo "c": {nx.single_source_dijkstra_path_length(G, "c")}')
    print(f't) Emitir el radio del grafo: {nx.radius(G)}')
    print(f'u) Emitir el diámetro del grafo: {nx.diameter(G)}')
    print(f'v) Emitir la excentricidad: {nx.eccentricity(G)}')
    print(f'w) Emitir el centro del grafo: {nx.center(G)}')
    print(f'x) Emitir la periferia del grafo: {nx.periphery(G)}')
    print(f'y) Emitir la densidad: {nx.density(G)}')
    print('z) Dibujar el grafo y emitir con matplotlib.pyplot:')

    #emitirGraph('Segundo Parcial Matematica III')

    R = nx.to_directed(G)
    confGraph(R)
    #emitirGraph('Grafo II')

    # Ejercicio 2
    texto = """
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""

    regex = r'".*"'
    otro_regex = r'\"[A-Z]+\W[\/A-Za-z0-9\s.-]+\"'

    sol_regex = re.findall(regex, texto)
    print(sol_regex)

    #  Ejercicio 3
    class Grafo:
        def __init__(self):
            self.G = nx.Graph()
        
        def agregar(self, nodos, edges, weigthed):
            self.G.add_nodes_from(nodos)
            self.G.add_edges_from(edges)
            self.G.add_weighted_edges_from(weigthed)
        
        def dibujar(self):
            labels = nx.get_edge_attributes(self.G, 'weight')
            pos = nx.shell_layout(self.G)
            nx.draw_networkx(self.G, pos)
            nx.draw_networkx_nodes(self.G, pos, node_size=600, node_color='skyblue', node_shape='h')
            nx.draw_networkx_edges(self.G, pos, edge_color='pink')
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_color='blue')

        def show(self, title):
            plt.title(title)
            plt.axis('off')
            plt.show()

    grafo1 = Grafo()
    grafo1.agregar(nodos, edges, weigthed_edges)
    grafo1.dibujar()
    grafo1.show('Grafo con clase')

    #Ejercico 4
    class Regex:
        def __init__(self, regex, texto):
            self.regex = regex
            self.texto = texto

        def print_regex(self):
            reg = re.findall(self.regex, self.texto)
            print(reg)

    regex1 = Regex(regex, texto)
    print("Clase Regex:\n")
    #regex1.print_regex()

if __name__ == '__main__':
    main()
