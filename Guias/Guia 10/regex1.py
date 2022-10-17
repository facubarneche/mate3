"""
1. En las tablas que siguen, cada fila de la tabla corresponde a una expresión regular; cada columna, a una cadena de caracteres. Completar esas tabla escribiendo SI o NO en cada una de sus celdas, según si la cadena que encabeza la columna pertenece o no al lenguaje representado por la expresión regular que encabeza la fila. Puede utilizarse cualquiera de las herramientas en línea que se brindaron.
"""

import re

def main():

    def regex(reg, string):
        print(reg)
        print (re.findall(reg, string), end='\n================================================\n')
    
    string1 = 'abc, bca, xxx, x, (xxx), (z+, 1a2b3, b34c, 123*, pan'
    print(string1, end='\n============================================\n')
    regex('[^abc]?', string1)
    regex('([^a][^b][^c])*', string1)
    regex('[^(abc)]+', string1)
    regex('\([^abc]\)*', string1)

    string2 = 'pa, Pan, PanN, PpAa, Pan*, Xan\*, |A|, \.\\, .\.*, .\an*'
    print(string2, end='\n============================================\n')
    regex('(Pp)(Aa)(Nn)*', string2)
    #regex('[P\p][A\a][N\n]*', string2) error mal escape
    regex('\.\\.*', string2)
    regex('[^Aa](an)\*', string2)

    string3 = '(ab), b7, b52s, [^ab], (x, b2s, (pe, bas?, ((, xxx'
    print(string3, end='\n============================================\n')
    regex('\([^ab)]', string3)
    regex('b[3-72]s', string3)
    regex('(([^a][^b])*)+', string3)
    regex('b[^0-59]s?', string3)

if __name__ == '__main__':
    main()
