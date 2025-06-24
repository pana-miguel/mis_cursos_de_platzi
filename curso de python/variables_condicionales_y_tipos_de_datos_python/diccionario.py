numbers = {1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco"}
print(numbers)
print(type(numbers))

print(numbers[3])

informacion ={"nombre": "miguel",
              "apellido": "angel",
              "altura": 1.75,
              "peso": 70,}

print(informacion)
del informacion["altura"] #esto da error porque no existe la clave edad
print(informacion)

claves = informacion.keys() #esto devuelve una vista de las claves del diccionario
print(claves)

values = informacion.values() #esto devuelve una vista de los valores del diccionario
print(values)

pairs = informacion.items() #esto devuelve una vista de los pares clave-valor del diccionario
print(pairs) 

contactos = { "miguel":{"apellido": "angel",
              "altura": 1.75,
              "peso": 70}, 
            "jose":{"apellido": "sierra",
              "altura": 1.95,
              "peso": 100}}

print(contactos["miguel"]) #esto devuelve el diccionario de miguel
print(contactos["jose"]) #esto devuelve el diccionario de jose