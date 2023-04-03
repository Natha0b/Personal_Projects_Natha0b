# Un for cumple multiples funciones pero en si se utiliza para iterar una lista de elementos.
#range crea una secuencia de numeros que podamos utilizar dentro de nuestro for
#Range es iterable
#String es iterable
# La variable numero va a tomar el valor de cada uno de los elementos que se encuentran dentro de range

buscar = 10

for numero in range(5): #range crea una secuencia de numeros que podamos utilizar dentro de nuestro for
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontre el numero buscado :(")

#De esta forma podemos imprimir cada uno de los careteres del string que le pasemos
for char in "Ultimate Python":
    print(char)