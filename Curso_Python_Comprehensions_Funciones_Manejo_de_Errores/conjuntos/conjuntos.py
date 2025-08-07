conjunto_paises = {'col','mex','bol'} #el conjunto se denomina con las llaves y si hay un elemento igual por ejemplo dos col solo deja uno 
print(conjunto_paises)
print(type(conjunto_paises))

conjunto_numeros = {1,2,3,4,66,888,12334,2,2,2}
print(conjunto_numeros)

conjunto_tipos = {1, 'hola', False, 12.5}
print(conjunto_tipos)

secmentar = set('adios')
print(secmentar)

set_tuplas = set(('abc','csv','as','abc'))
print(set_tuplas)

numeros = [1,2,3,45,5,6,7,2,3,4,5,1]
print(numeros)
set_numeros = set(numeros) #pasa la lista a conjunto
print(set_numeros)

numeros_unicos = list(set_numeros) #pasa el conjunto a lista
print(numeros_unicos)