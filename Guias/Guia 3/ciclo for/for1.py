#1. Escribe un programa que le permita realizar la escritura de los primeros 100 números naturales.

def main():
    #Esta forma me parece mas eficaz, pero la guia es de bucles for
    #print(list(range(101)))

    for i in range(101):
        print(i, end = ", ")

if __name__ == "__main__":
    main()
