def main():
    print("PRUEBA 4")
    array = [1,2,3,4,5,6,7,8,9,10]
    nombre = input ("Escriba su nombre: ").capitalize()
    apellido = input("Enter your lastName: ").capitalize()
    edad = input(f"Enter your Age {nombre} {apellido}: ")
    print(f"¡Hola, {nombre}, {apellido}, pa, acordate que tenes {edad} años papuuu!")

    if nombre == "Alejo" or apellido == "Meni":
        print("Hijo de puta, hijo de puta, hijo de puta, (clap clap clap clap)")

    for i in  array:
        print(f"hola tu num es: {i}")


    print('Hola "todo bien?"')

if __name__ == "__main__":
    main()
