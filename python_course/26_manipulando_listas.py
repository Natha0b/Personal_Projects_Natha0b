mascotas = ["Africa", "Moscu", "Tokio", "Moschino"]
print(mascotas[0]) #De esta forma ponemos el indice del elemento al cual queremos acceder en este conetxto accederiamos al elemento de Africa.

#De esta forma cambiamos un elemento de la lista 
mascotas[0] = "Kiara"
print(mascotas)

#De esta forma obtenemos una parte parcial de la lista 
print(mascotas[0:3])
print(mascotas[-1])
print(mascotas[::2]) #Poniendo los dos puntos le decimos que nos omita o salte lo que no queremos imprimir 


numeros = list(range(21))
print(numeros[::2]) #De esta forma podemos darle la opcion de solo imprimir los numeros pares que tenemos en nuestra lista
print(numeros[1::2]) #De esta forma podemos darle la opcion de solo imprimir los numeros impares que tenemos en nuestra lista 



