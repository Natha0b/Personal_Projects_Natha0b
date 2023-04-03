# El return me permite asignarle a una variable fuera de la funcion para poder usarla en otras ocaciones
# Return es una palabra recervada que nos permite tomar la variable y devolverla en otras ocaciones
def suma(a, b):
    resultado = a + b
    return resultado

c = suma(1, 2)
d = suma(c, 2)

print(d)