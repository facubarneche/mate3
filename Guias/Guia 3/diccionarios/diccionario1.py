#1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar).
#Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. No se podrán ingresar nombres repetidos.

def main():
    stop = False

    user = {
        'Facundo' : 1534352122
    }

    while stop is False:
        new_user = input('Ingrese un nuevo usuario: ')
        new_phone = int(input(f'Ingrese el telefono de {new_user}: '))

        user[new_user] = new_phone

        quest = input('Ingrese "S" para finalizar, y enter para continuar: ').upper()

        if quest == 'S':
            stop = True

    print(user)

if __name__ == '__main__':
    main()
