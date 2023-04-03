#and - Lo usamos cuando tenemos dos condiciones cuando las dos sean true el resultado sera true pero si una falla va a ser false
#or - Lo usamos cuando tenemos dos condiciones pero cuando una es true el resultado completo va a ser true y para que sea false deben ser ambas false
#not - Lo que hace es negar el resultado de una operación

gas = True
encendido = True
edad = 18

if gas and encendido: #En este caso ambos deben ser True
    print("Puedes avanzar")

if gas or encendido: #En este caso solo con que una sea true imprimiria el mensaje
    print("Puedes avanzar")

if not gas or encendido: #En este caso la negacion convertira la variable en true e imprimira el mensaje 
    print("Puedes avanzar")

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas and (encendido or edad > 17):
    print("Puedes avanzar")


if not gas and (encendido or edad > 17):
    print("Puedes avanzar")


# Operadores de corto circuito 
# Estas operaciones se ejecutan de izquierda a derecha
# es importante ya que si la primera evaluacion que
# realice el codigo es falsa simplemente no realiza las
# demas que tenga en la misma linea


if not gas and encendido and edad > 17:
    print("Puedes avanzar")
