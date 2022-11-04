"""
5. Dado el archivo pedidos.txt. Escribe un nuevo archivo 'pedidos_agrupados.tx
t', en el que los datos se reagrupen de la siguiente manera:
1289,T83456
1289,Z22334
1205,T10032
1205,B77301
1205,T10786
1205,C77502
1410,K34001
1410,T98987
Sugerencia para abrir el archivo: txt = open("<ruta>/pedidos.txt").read()
Sugerencia para escribir el archivo: open("pedidos_agrupados.txt", "w")
"""

import re

def main():
    
    txt = open('Clases/Unsam.Clase.10/regex_archivos/pedidos.txt').read()
    txt2 = open("Clases/Unsam.Clase.10/regex_archivos/pedidos_agrupados.txt", "w")

    reg = '[\d]+[\W\S][A-Z]?'

    def regex(rex, text):
        return re.findall(rex, text)
    
    toAgrupados = regex(reg, txt)
    print(toAgrupados)

    txt2.write('asd')

if __name__ == '__main__':
    main()
