#3. Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen al primero pero noal segundo, sin repetir ninguno. Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolverá la lista [1].

def main():
    
    conj1 = {1, 2, 1}
    conj2 = {2, 3, 2, 4}

    only_conj1 = conj1 - conj2

    print(only_conj1)


if __name__ == '__main__':
    main()
