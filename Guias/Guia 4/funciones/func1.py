"""
1.El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?
def maximo(a, b):
if x > y:
return x
else:
return y
def minimo(a, b):
if x < y:
return x
else:
return y
x = int(input("Ingrese un número:\n"))
y = int(input("Ingrese otro número:\n"))
print(maximo(x-3, minimo(x+2, y-5)))
"""

def main():

    def maximo(x, y):
        if x > y:
            return x
        else:
            return y
    
    def minimo(x, y):
        if x < y:
            return x
        else:
            return y

    x = int(input("Ingrese un número:\n"))
    y = int(input("Ingrese otro número:\n"))
    print(maximo(x-3, minimo(x+2, y-5)))

if __name__ == '__main__':
    main()
