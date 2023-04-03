# Los xargs nos permiten tomar todos los argumentos que tengamos en una funcion
# El asterisco nos define que es un parametro iterable 
#Es importante fijarse en la identacion de nuestras lineas ya que eso podria arrojarnos un error
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
