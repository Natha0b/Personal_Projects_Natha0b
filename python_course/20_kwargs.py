#Los kwargs se trabajan con doble asterisco
#Al trabajar con los kwargs siempre debemos definir los argumentos que le vamos a pasar a la funcion
def get_product(**datos):
    print(datos[id], datos["name"])

get_product(id="id", name="iphone", desc="Esto es un celular")