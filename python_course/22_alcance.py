saludo = "Hola Global"
def saludar():
    global saludo
    saludo = "Hola Mundo"

def saludachanchito():
    saludo = "Hola Chanchito"


print(saludo)
saludar()
print(saludo)
