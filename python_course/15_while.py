# Ejemplo de como usar un while
numero = 1

while numero < 100:
    print(numero)
    numero *= 2


#Terminal virtual

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

#loop infinitos

comando = ""

while True: #Cuando tenemos un while el cual sabemos que tiene un ciclo infinito debemos siempre terminar nuestra condicion con break el cual se encargue de cortar con ese ciclo infinito
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break


