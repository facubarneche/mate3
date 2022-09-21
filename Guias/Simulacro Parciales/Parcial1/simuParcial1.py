"""
En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan fútbol, 50 entrenan squash 
y 60 entrenan tenis. 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
Si 10 deportistas entrenan los tres deportes 
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

lista_futbol = [3, 5, 10, 12]
tupla_squash = (10, 20, 15, 5)
diccio_tenis = {"infantil": 12,  "juniors": 10,
                "adolescentes": 20, "adultos": 18}

universal = 100
ninguno = 0 #Entiendo que no hay ninguno fuera de los conjuntos ya que son "deportistas"

##################################################################################
# Compruebo los datos dados con las consignas
##################################################################################

def check(deporte, nombreDeporte):
    total = 0

    for cant in deporte:
        total += cant
    
    print(f'La cantidad total que hacen {nombreDeporte} es de {total}')
#FinDef

def checkDictionary(deporte, nombreDeporte):
    total = 0

    for cant in deporte.values():
        total += cant
    
    print(f'La cantidad total que hacen {nombreDeporte} es de {total}')
#FinDef

check(lista_futbol, 'Futbol')           #Futbol correcto! 30
check(tupla_squash, 'Squash')           #Squash correcto! 50
checkDictionary(diccio_tenis, 'Tenis')  #Tenis correcto! 60

##################################################################################
# Paso todo a Set
##################################################################################

setFutbol = set(lista_futbol)
setSquash = set(tupla_squash)
setTenis = set(diccio_tenis.values())

print(f'futbol => {setFutbol} de tipo {type(setFutbol)}')
print(f'squash => {setSquash} de tipo {type(setSquash)}')
print(f'tenis => {setTenis} de tipo {type(setTenis)}')

##################################################################################
# Resuelvo
##################################################################################

def all(sport1, sport2, sport3):                    #Funcion para la interseccion de los 3 deportes
    return sport1 & sport2 & sport3
#FinDef

def only2(sport1, sport2):                          #Funcion para obtener interseccion de 2 deportes
    return (sport1 & sport2) - futbol_squash_tenis
#FinDef

def only1(sport1, sport2, sport3):                  #Funcion para obtener los que hacen solo 1 deporte
    return (sport1 - sport2) & (sport1 - sport3)
#FinDef

def pregunta4(sport1, sport2):                      #Funcion para responder futbol o tenis
    suma = 0
    sport1_sport2 = sport1 | sport2
    
    for cant in sport1_sport2:
        suma += cant
    
    return suma
#FinDef

futbol_o_tenis = pregunta4(setFutbol, setTenis)


#Agrego a variables los valores buscados
futbol_squash_tenis = all(setFutbol, setSquash, setTenis)   #La interseccion de los 3 deportes
futbol_squash = only2(setFutbol, setSquash)                 #La interseccion de futbol y squash
futbol_tenis = only2(setFutbol, setTenis)                   #La interseccion de futbol y tenis
tenis_squash = only2(setTenis, setSquash)                   #La interseccion de tenis y squash
futbol = only1(setFutbol, setSquash, setTenis)#La inter de la resta de futbol con los otros 2 deportes
squash = only1(setSquash, setFutbol, setTenis)#La inter de la resta de squash con los otros 2 deportes
tenis = only1(setTenis, setFutbol, setSquash) #La inter de la resta de tenis con los otros 2 deportes

##################################################################################
# Gráfico de resultados
##################################################################################
# preparamos la ventana del gráfico
plt.figure('Ejemplo de primer parcial ')

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Futbol", "Squash", "Tenis"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(futbol)
diagram.get_label_by_id('010').set_text(squash)
diagram.get_label_by_id('001').set_text(tenis)
diagram.get_label_by_id('110').set_text(futbol_squash)
diagram.get_label_by_id('011').set_text(tenis_squash)
diagram.get_label_by_id('101').set_text(futbol_tenis)
diagram.get_label_by_id('111').set_text(futbol_squash_tenis)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universal}",
         size=10)

plt.text(0.40, -0.5,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {ninguno}",
         size=8)

# Respondemos las preguntas
plt.text(-1.10, -0.20,
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s="Entrenan sólo tenis = " + str(tenis),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s="Entrenan sólo fútbol = " + str(futbol),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="Entrenan sólo squash = " + str(squash),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Entrenan tenis o fútbol = " + str(futbol_o_tenis),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')  # Recuadro
plt.title("Deportistas")
plt.show()
##################################################################################
# Fin de programa
##################################################################################