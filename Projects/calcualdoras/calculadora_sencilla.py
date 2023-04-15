print("Bienvenidos a la calculadora")
print("Para salir, escribe exit")
print("Las operaciones son: Suma, Resta, Multiplicación y Division")

resultado =""
while True:
    if not resultado:
        resultado = input("ingrese un número: ")
        if resultado.lower() == "exit":
            break
        resultado = int(resultado)
    print("Las operaciones son: suma, resta, multi y div")
    op = input("Ingrese la opercion: ")
    if op.lower() == "exit":
        break

    n2 = input("Ingrese el siguiente número: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida!")
        break
    
    print(f"El resultado es {resultado}")