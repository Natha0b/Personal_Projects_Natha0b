mascotas = [
    "Africa", 
    "Moscu", 
    "Tokio", 
    "Moschino",
    "Chanchito",
    "Canela"
    ]

#Con el metodo insert podemos añadir elementos a nuestra lista
#Con el metodo append podemos añadir elementos a nuestra lista estos se añadiran al final 
mascotas.insert(1, "Melvin")
mascotas.append("Lolita")


#Con el metodo remove podemos eleminar elemento que se encuentran dentro de una lista 
#Lo hacemos colocando el elemento que deseamos eliminar no el indice o ubicacion de dicho elemento

mascotas.remove("Chanchito")

#Para eliminar un elemento por medio de su indice podemos usar el metodo de pop
mascotas.pop(1)

#Tambien podemos hacerlo usando la palabra recervada de del
del mascotas[0]

#Para limpiar todo nuestro arreglo o nuestra lista usamos el metodo de clear y este se encagara de devolvernos la lista vacia
mascotas.clear()
print(mascotas)
