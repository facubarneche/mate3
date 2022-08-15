
un_texto = "Me gusta Python"
id(un_texto)
print(un_texto)

def mi_funcion(mi_variable):
    print("Id de <mi_variable> dentro de la función: {}, mi_variable: {}\n".format(id(mi_variable),mi_variable))
    
mi_funcion(un_texto)


mi_variable_inmutable = "Me gusta Python"
print("mi_variable_inmutable (id: {}): {}\n".format(id(mi_variable_inmutable), mi_variable_inmutable))

def mi_funcion(var_de_func):
    print("var_de_func antes de retornar (id: {}): {}\n".format(id(var_de_func), var_de_func))
    var_de_func += ", y a vos?"
    print("var_de_func (id: {}): {}\n".format(id(var_de_func), var_de_func))
    return var_de_func

retorno_de_funcion = mi_funcion(mi_variable_inmutable)
print("retorno_de_funcion (id: {}): {}\n".format(id(retorno_de_funcion),retorno_de_funcion))

print("mi_variable_inmutable después de función (id: {}): {}\n".format(id(mi_variable_inmutable), mi_variable_inmutable))