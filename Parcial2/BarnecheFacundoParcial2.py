#1.	Dada la siguiente matriz que determina nodos, pesos y conexiones:
"""
    A   B   C   D   E   F   G   H
A               6
B           1       3       7
C                               8
D                       5   4
E   3           2
F                           8
G                           9
H                               1

"""

#Imports
import networkx as nx
import matplotlib.pyplot as plt
import re

#Creo la clase grafo
class Grafo:
    #Creo el constructor
    def __init__(self):
        self.G = nx.Graph()
    
    #Metodo para agregar nodos, edges y los pesos al grafo
    def agregarAlGrafo(self, nodos, edges, weigth):
        self.G.add_nodes_from(nodos)
        self.G.add_edges_from(edges)
        self.G.add_weighted_edges_from(weigth)

    #Metodo para dibujar el grafo
    def dibujarGrafo(self):
        pos = nx.shell_layout(self.G) #Posiciona a los nodos con un respectivo layout 
        labels = nx.get_edge_attributes(self.G, 'weight')#Obtiene los pesos para usar como etiquetas
        nx.draw_networkx(self.G, pos=pos)
        nx.draw_networkx_nodes(self.G, pos=pos, node_size=800, node_color='skyblue')
        nx.draw_networkx_edges(self.G, pos=pos,edge_color='orange')
        nx.draw_networkx_edge_labels(self.G, pos=pos, edge_labels=labels, font_color='blue')
        nx.draw_networkx_labels(self.G, pos=pos)

    def contestarConsignas(self):
        #b)Emitir los vecinos de "b"
        print(f'Vecinos de "B": {list(nx.neighbors(self.G, "B"))}')
        #c)Emitir cantidad de aristas de cada nodo
        print(f'Cantidad de aristas de cada nodo: {self.G.degree()}')
        #d)Convertir en diccionaro el punto anterior
        print(f'Cantidad de aristas de cada nodo con diccionario: {dict(self.G.degree())}')   
        #e)Crear y emitir la matriz de adyacencia
        #Creo la matriz de adyacencia
        A = nx.adjacency_matrix(self.G)
        #Emito la matriz de adyacencia
        print(f'Matriz de adyacencia:\n{A.todense()}')   
        #f)Crear y emitir la matriz de incidencia utilizando el atributo de pesos y sin ellos: 
        #Creo la matriz de incidencia sin peso
        I = nx.incidence_matrix(self.G)
        #Emito la matriz de incidencia sin el atributo pesos
        print(f'Matriz de incidencia sin peso:\n{I.todense()}')
        #Creo la matriz de incidencia con peso
        IP = nx.incidence_matrix(self.G, weight='weight')
        #Emito la matriz de incidencia con el atributo pesos
        print(f'Matriz de incidencia con peso:\n{IP.todense()}')
        #g)Emitir la ruta mas corta desde "g"
        #Cabe destacar que la ruta mas corta es la que tiene menos aristas
        print(f'Ruta mas corta desde "G": {nx.single_source_shortest_path(self.G, "G")}')
        #h)Emitir longitud desde "H":
        print(f'Longitud de ruta mas corta desde "H": {nx.single_source_shortest_path_length(self.G, "H")}')
        #i)Emitir el promedio de la ruta mas corta usando el metodo de Bellman-Ford
        print(f'Promedio de la ruta mas corta con el metodo Bellman-Ford: {nx.average_shortest_path_length(self.G, method="bellman-ford")}')
        #j)Emitir la ruta ponderada mas corta entre "G" y "H" usando el algoritmo de Dijkstra
        #Se destaca que este algoritmo se calcula en base al peso y no a la cantidad de aristas
        print(f'La ruta mas corta usando el algoritmo de Dijkstra entre "G" y "H": {nx.algorithms.dijkstra_path(self.G, "G", "H")}')
        #k)Emitir la longitud de la ruta ponderada entre "H" y "G" usando el algoritmo de Dijkstra
        print(f'La longitud de Ruta ponderada más corta entre "H" y "G": {nx.algorithms.dijkstra_path_length(self.G, "H", "G")}')
        #l)Emitir la longitud de la ruta desde el nodo "C" utilizando Dijkstra
        print(f'La longitud de Ruta ponderada más corta desde el nodo "C": {nx.algorithms.single_source_dijkstra_path_length(self.G, "C")}')
        #m)Emitir el radio del grafo
        print(f'El radio es: {nx.radius(self.G)}')
        #n)Emitir el diametro del grafo
        print(f'El diametro es: {nx.diameter(self.G)}')
        #o)Emitir la excentricidad
        print(f'La excentricidad es: {nx.eccentricity(self.G)}')
        #p)Emitir el centro del grafo
        print(f'El centro del grafo es: {nx.center(self.G)}')
        #q)Emitir la periferia del grafo
        print(f'La periferia del grafo es: {nx.periphery(self.G)}')
        #r)Emitir la densidad
        print(f'La densidad es: {nx.density(self.G)}')
        #s) Esta afuera de la funcion
        
    def mostrarGrafo(self, title):
        plt.title(title)
        plt.axis('off')
        plt.show()


#Creo las variables de nodos, enlaces y pesos de enlace para luego llenar el grafo
nodos = ['A','B','C','D','E','F','G','H']
edges = [('A','D'),('B','C'),('B','E'),('B','G'),('C','H'),('D','F'),('D','G'),('E','A'),('E','D'),('F','G'),('G','G'),('H','H')]
weigth = [('A','D',6),('B','C',1),('B','E',3),('B','G',7),('C','H',8),('D','F',5),('D','G',4),('E','A',3),('E','D',2),('F','G',8),('G','G',9),('H','H',1)]

#Creo una instancia de la clase Grafo
G = Grafo()

#Le agrego los nodos, enlaces y pesos de enlaces al grafo con su metodo
G.agregarAlGrafo(nodos, edges,weigth)

#Dibujo el grafo para luego mostrarlo
G.dibujarGrafo()

#Contesto las consignas del grafo
G.contestarConsignas() 

#Imprimo el grafico del grafo
G.mostrarGrafo('Segundo Parcial Matemática III')

#Le pregunte a Monica y me dijó que cree un nuevo grafo afuera para este punto
#s)Convertir el grafo dirigido
G1 = nx.Graph()
G1.add_nodes_from(nodos)
G1.add_edges_from(edges)
G1.add_weighted_edges_from(weigth)

#Redirigo el grafo 
R = G1.to_directed()
#Agreg configuraciones y dibujo el nuevo digrafo
pos = nx.shell_layout(G1) #Posiciona a los nodos con un respectivo layout 
labels = nx.get_edge_attributes(G1, 'weight')#Obtiene los pesos para usar como etiquetas
nx.draw_networkx(R, pos=pos)
nx.draw_networkx_nodes(R, pos=pos)
nx.draw_networkx_edges(R, pos=pos)
nx.draw_networkx_edge_labels(R, pos=pos, edge_labels=labels)
nx.draw_networkx_labels(R, pos=pos)
plt.title('Grafo redirigido (DiGrafo)')
plt.axis('off')
plt.show()

"""
3.	Dadas las siguientes líneas de texto:

"1","2015-000001","2015-01-01","11:38:36","hawaiian","M","classic",13.25
"2","2015-000002","2015-01-01","11:57:40","classic_dlx","M","classic",16
"3","2015-000002","2015-01-01","11:57:40","mexicana","M","veggie",16
"4","2015-000002","2015-01-01","11:57:40","thai_ckn","L","chicken",20.75
"5","2015-000002","2015-01-01","11:57:40","five_cheese","L","veggie",18.5
"6","2015-000002","2015-01-01","11:57:40","ital_supr","L","supreme",20.75
"7","2015-000003","2015-01-01","12:12:28","prsc_argla","L","supreme",20.75

Hallar la expresión regular para extraer:

['hawaiian', 'classic_dlx', 'mexicana', 'thai_ckn', 'five_cheese', 'ital_supr', 'prsc_argla']
"""

#Creo clase para Regex
class Regex:
    def __init__(self, texto, regex):
        self.texto = texto
        self.regex = regex
    
    def filtrar(self):
        print(re.findall(self.regex, self.texto))


texto = """
"1","2015-000001","2015-01-01","11:38:36","hawaiian","M","classic",13.25
"2","2015-000002","2015-01-01","11:57:40","classic_dlx","M","classic",16
"3","2015-000002","2015-01-01","11:57:40","mexicana","M","veggie",16
"4","2015-000002","2015-01-01","11:57:40","thai_ckn","L","chicken",20.75
"5","2015-000002","2015-01-01","11:57:40","five_cheese","L","veggie",18.5
"6","2015-000002","2015-01-01","11:57:40","ital_supr","L","supreme",20.75
"7","2015-000003","2015-01-01","12:12:28","prsc_argla","L","supreme",20.75
"""

regex = "[a-z_]{8,}"

#Inicializo una instancia de la clase Regex
filtrado = Regex(texto, regex)
#Uso el metodo que devuelve el texto filtrado
filtrado.filtrar()