punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])


print(punto)
punto["x"] = 25

for valor in punto:
    print(valor,punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "chanchito"}
    {"id": 2, "nombre": "felix"}
    {"id": 3, "nombre": "carla"}
    {"id": 4, "nombre": "pepeganga"}
]