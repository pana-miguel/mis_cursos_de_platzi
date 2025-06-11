print("Nunca", "pares", "de", "aprender") #uso delas comas
#resulrado: Nunca pares de aprender

print("Nunca" + "pares" + "de" + "aprender")  #uso del signo + para concatenar
#resulrado: Nuncaparesdeaprender

print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender") #uso del signo + para concatenar con espacios
#resulrado: Nunca pares de aprender

print("Nunca", "pares", "de", "aprender", sep=", ") #uso del sep para cambiar el separador
#resulrado: Nunca, pares, de, aprender

print("Nunca", end=" ")
print("pares de aprender") #uso del end para cambiar el final de la linea
#resulrado: Nunca pares de aprender

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author) #uso de variables para almacenar valores
#resulrado: Frase: Nunca pares de aprender Autor: Platzi

frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}") #uso de f-strings para formatear cadenas
#resulrado: Frase: Nunca pares de aprender, Autor: Platzi

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author)) #uso de format para formatear cadenas
#resulrado: Frase: Nunca pares de aprender, Autor: Platzi

valor = 3.14159
print("Valor: {:.2f}".format(valor)) #uso de format para formatear cadenas con decimales
#resulrado: Valor: 3.14

print("Hola\nmundo")  #uso de \n para saltar de linea
#resulrado: Hola
#         mundo

print('Hola soy \'Carli\'') #uso de \' para escapar comillas simples
#resulrado: Hola soy 'Carli'

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") #uso de \\ para escapar la barra invertida
#resulrado: La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt
