#2. Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen a una o a otra, pero sin repetir ninguno. Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolverá el conjunto [1, 2, 3,4].

def main():

    conj1 = {1, 2, 1}
    conj2 = {2, 3, 2, 4}

    union = conj1 | conj2

    print(union)

if __name__ == '__main__':
    main()
