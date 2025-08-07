import random

countries = ['col','mex','bol','pe']
poblacion2 = {country: random.randint(1, 100) for country in countries}
print(poblacion2)

resultado = {pais: poblacion for (pais, poblacion) in poblacion2.items() if poblacion > 20}
print(resultado)


texto = 'hola, soy jose'
vocales = {c for c in texto if c in 'aeiou'}
print(vocales) #solo muestra una vez el elemento porque en este caso la o se repite 3 veces pero solo pone una 