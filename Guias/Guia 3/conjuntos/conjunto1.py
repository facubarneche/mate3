#1. Diseña un programa que reciba dos conjuntos y devuelva los elementos comunes a ambas, sin repetir ninguno. Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolverá 2.

def main():

    conj1 = {1, 2, 1}
    conj2 = {2, 3, 2, 4}
    
    inter = conj1 & conj2

    print(inter)

if __name__ == '__main__':
    main()
