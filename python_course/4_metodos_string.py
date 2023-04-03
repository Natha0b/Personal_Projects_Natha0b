animal = "chanCHito feliz"
print(animal.upper()) #Pasar el string a mayuscula
print(animal.lower()) #pasa el string a minuscula
print(animal.strip().capitalize()) #Toma la primera letra del string y la pasa a mayuscula y para algunos casos usar el strip el cual quita los espacios del lado derecho e izquierdo
print(animal.title()) #Pone mayusculas las letras del inicio de una palabra
print(animal.strip()) #Elimina los espacion del lado derecho e izquierdo del string
print(animal.lstrip()) #Elimina los espacios del lado izquierdo del string
print(animal.rstrip()) #Elimina los espacios del lado derecho del string
print(animal.find("CH")) #Devuelve la cantidad de caracteres del string que le pasemos
print(animal.replace("ch", "j")) #remplaza los caracteres que le pasemos en el string
print("nCH" in animal) #Devuelve un booleano para saber si se ecuentra un caracter en el string
print("nCH" not in animal) # devuelve un booleanos para saber si no se encuentra un caracter en el string
