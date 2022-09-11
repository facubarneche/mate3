"""
2.Convertir a funciones los siguientes ejercicios:

a.Práctica de rangos-listas-for-while:
a) Ejercicio 6 de rangos
b) Ejercicio 6 de listas
c) Ejercicio 3 y 4 de ciclo for
d) Ejercicio 7 de ciclo while

"""

from types import new_class


def main():
#a.a) Escribe un programa que pida dos números enteros y emita la lista de números pares entre ellos (incluidos ellos mismos si son pares)
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese otro numero: '))
    
    def listEven(num1, num2):

        if(num1 % 2 == 0):
            print(list(range(num1, num2, 2)))
        else:
            print(list(range(num1 + 1, num2, 2)))

    listEven(num1, num2)

#a.b) Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (crear una lista distinta).

    list1 = []
    num = int(input('Ingrese la cantidad de palabras a agregar: '))

    for i in range(num):
        list1.append(input(f'Ingrese la palabra {i + 1}: '))

    def spinList(array):
        newArray = array.copy()
        newArray.reverse()
        return newArray
    #finDef

    print(spinList(list1))

#a.c) Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado.
    #Muestre los N primeros números de la secuencia de Fibonacci, siendo n un dato entero.

    num = int(input('Ingrese un numero: '))

    def fact(num):
        fac = 1
        for i in range(1, num + 1):
            fac *= i

        return fac

    print(f'El factorial de {num} es {fact(num)}')

    def fibonacci(num):
        a, b = 0, 1

        for i in range(num + 1):
            print(f'{a}, ', end = "")
            a, b = b, a + b

    fibonacci(num)
    print("")

#a.d) Escribe un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos. El programa terminará cuando se escriba un número que no esté comprendido entre los dos valores iniciales y emitirá la cantidad de números ingresados.

    min = int(input('Ingrese un numero minimo: '))
    max = int(input('Ingrese un numero maximo: '))

    while True:
        nums = int(input('Escribe numeros entre el minimo y el maximo: '))

        if(nums < min or nums > max):
            break


if __name__ == '__main__':
    main()
