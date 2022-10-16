"""
Ejercicio 1. Dada la clase
class Maquina:
    nombre = ''
    id = ''
    fecha='' # fecha de puesta en marcha

Define los métodos:
a. parar, que emitirá el mensaje 'ZZZZzzzzzzzzz'
b. marchar, que emitirá el mensaje 'blablablaaaaa'
c. contar, que emitirá el mensaje '1,2,3,4,…' (enteros positivos, mayores a 0, hasta el tope que le indiques)
d. emitir, que emitirá el nombre dado a la máquina y la edad en función de la fecha de puesta en marcha.
El programa deberá pedir al usuario:
a. si desea crear una máquina, en el caso de que su respuesta sea afirmativa, instanciar el objeto.
b. que le dé un nombre, id, fecha de puesta en marcha.
c. que le indique si quiere que emita su nombre.
d. que le indique si quiere que lo ponga en marcha.
e. que le indique si quiere que lo pare.
f. que le indique si quiere escucharlo contar pero debe decirle hasta qué número.
"""

from datetime import date

def main():

    class Maquina:
        def __init__(self, nombre, id, fecha):
            self.nombre = nombre
            self.id = id
            self.fecha = fecha
        #FinConstruct

        def parar(self):
            return 'ZZZZzzzzzzzzz'
        #FinDef

        def marchar(self):
            return 'blablablaaaaa'
        #FinDef

        def contar(self, tope):
            return list(range(tope))
        #FinDef

        def emitir(self):
            msg = "Nombre: " + self.nombre + "\nEdad: " + str(date.today().year - self.fecha.year) 
            return msg
        #FinDef

    #FinClass


    #Pruebas de lo pedido
    
    #Se crea una instancia de Maquina
    instanciarObjeto = int(input('Desea crear una maquina?\n1.Si 2.No\n'))

    if(instanciarObjeto == 1):
        nombre = input('Ingrese el nombre de la cortadora: ')
        id = int(input('Ingrese el id de la maquina: '))
        dia = int(input('Ingrese el dia de puesta en marcha: ' ))
        mes = int(input('Ingrese el mes de puesta en marcha: ' ))
        año = int(input('Ingrese el año de puesta en marcha: ' ))
        maquina1 = Maquina(nombre, id, date(año,mes,dia))

        print(maquina1.nombre)
        print(maquina1.parar())
        print(maquina1.marchar())
        print(maquina1.contar(20))
        print(maquina1.emitir())

    else:
        print('Hasta luego')


if __name__ == '__main__':
    main()
