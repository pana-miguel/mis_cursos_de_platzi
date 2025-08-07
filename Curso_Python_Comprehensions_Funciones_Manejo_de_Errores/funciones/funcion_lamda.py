def incrementar(x):
    return x + 1

increment2 = lambda x : x + 1 #funcion con sintaxis mas corta que se puede asignar a una variable o pasar como argumento a otra funcion

print(incrementar(5))
print(increment2(5))


nombre_completo = lambda nombre, apellido: f'su nombre competo es {nombre} {apellido}'

text = nombre_completo('miguel', 'sierra')
print(text)