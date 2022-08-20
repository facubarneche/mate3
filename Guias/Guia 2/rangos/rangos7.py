"""7. Escribe tres programas que emitan las siguientes secuencias de números:
 En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento.
 En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos.
 En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos."""

def main():
    print(list(range(10)))
    print(list(range(-1, 10)))
    print(list(range(3, 13, 3)))


if __name__ == "__main__":
    main()
