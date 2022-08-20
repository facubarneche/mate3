una_lista = ["una cosa","dos cosas","tres cosas"]
print(una_lista)
id(una_lista)

una_lista[1]= "que cosa?"
print(una_lista)
id(una_lista)

una_lista = una_lista + ["más cosas"]
print(una_lista)
id(una_lista)

otra_lista = una_lista
print(otra_lista)
id(otra_lista)

otra_lista = otra_lista + ["una más"]
print(otra_lista)
id(otra_lista)

print(una_lista)
id(una_lista)


una_lista.append("Python")
print(una_lista)
id(una_lista)

print(otra_lista)
id(otra_lista)

una_lista = ["una cosa","dos cosas"]
print(una_lista)
id(una_lista)

def mi_funcion(mi_variable):
    print("Id de <mi_variable> dentro de la función: {}, mi_variable: {}\n".format(id(mi_variable),mi_variable))
    mi_variable += ["tres cosas"]
    print("Id de <mi_variable> dentro de la función \ndespués de la modificación: {}, mi_variable: {}\n".format(id(mi_variable),mi_variable))
    
mi_funcion(una_lista)
print("Id de <una_lista> fuera de la función: {}, una_lista: {}\n".format(id(una_lista),una_lista))