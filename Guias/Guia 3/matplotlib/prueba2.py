import matplotlib.pyplot as plt

def main():

    #Creamos 2 listas con datos para el grafico
    x = ['Python', 'Java', 'C', 'C++', 'Matlab', 'Octave']
    usuarios = [10, 7, 15, 8, 9, 7]

    #Uso de la capa de artista
    fig = plt.figure() #Se crea una figura
    ax = fig.add_subplot(111) ##Creamos los objetos Axes
    #El numero 111 significa que solo queremos una trama

    #Interfaz orientada a objetos
    #ax es el objetivo y los elementos de grafico se agregan utilizando diferentes metodos de este objeto
    ax.bar(x, usuarios)
    ax.set_title('Usuarios de Lenguajes de Programacion')
    ax.set_xlabel('Lenguaje de Programacion')
    ax.set_ylabel('Numero de usuarios')
    plt.show()

if __name__ == '__main__':
    main()
