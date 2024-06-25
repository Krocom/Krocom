# Ejemplo de diccionario con lista
personas= []
datosPersona = {
    "nombre": "Juan",
    "apellido": "Garcia",
    "edad": 30,
    "ciudad": "Buenos Aires",
    "jubilado": False,
    "hijos": ["Ana", "Fernando", "Marcela"]
}
personas.append(datosPersona)

datosPersona = {
    "nombre": "Ana",
    "apellido": "Lopez",
    "edad": 30,
    "ciudad": "Buenos Aires",
    "jubilado": False,
    "hijos": ["Ana", "Fernando", "Marcela"]
}
personas.append(datosPersona)

print(personas[0]["nombre"],end=", ")
print(personas[0]["apellido"])
print(personas[1]["nombre"],end=", ")
print(personas[1]["apellido"])