numeros = [2, 4, 1, 45, 75, 22]

#Para odernar una lista utlizamos el metodo sort
numeros.sort()

#Para que la lista se ordene al reves o de forma descendente simplemente le pasamos un argumento a nuestro metodo sort
numeros.sort(reverse=True)

#El metodo sorted nos devulve una nueva lista sin afectar las lista que ya tenemos predeterminada
numeros2 = sorted(numeros)

print(numeros)
print(numeros2)

#Para ordenar listas que conetienen listas usamos el metodo de sort
#Se ordena con este metodo siempre y cuando el primer elemento dentro de la lista se ordenble ej: numeros, ya que de lo contrario no lo ordenara
usuarios = [
    [4, "Africa"]
    [1, "Kiara"]
    [5, "Moscu"]
]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)

#La funcion lambda se encarga de acceder al segundo elemento de un listado
#Esta funcion la usamos solo en casos puntuales en los que el crear una funcion como la anterior y no la vamos a volver a usar en nuestro codigo 
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)