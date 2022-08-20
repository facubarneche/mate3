#8. Escribe un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números. Para indicar que quiere seguir escribiendo números, el usuario deberá contestar ‘S’ o ‘s’ a la pregunta.

def main():
    quest = 'S'
    
    while quest == 'S':
        num = int(input('Ingrese un numero par: '))

        while num % 2 != 0:
            num = int(input('El numero debe ser par, pruebe de nuevo con otro numero: '))

        quest = input('Ingrese "S" para continuar, en caso contrario finalizara el programa: ').upper()
if __name__ == '__main__':
    main()
