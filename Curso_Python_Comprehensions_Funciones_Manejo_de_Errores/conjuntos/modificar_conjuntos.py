conjunto_paises = {'col','mex','bol'} #el conjunto se denomina con las llaves y si hay un elemento igual por ejemplo dos col solo deja uno 

tamanio_conjunto = len(conjunto_paises)
print(tamanio_conjunto)

print('col' in conjunto_paises) #mirar si esta dentro de un conjunto
print('pe' in conjunto_paises)

conjunto_paises.add('pe')
print(conjunto_paises)
print('pe' in conjunto_paises)

conjunto_paises.update(['can','uru','arg']) #agrega un conjunto a el conjunto que queramos 
print(conjunto_paises)

conjunto_paises.remove('col') #elimina un elemento del conjunto
print(conjunto_paises)
#si no hay un elemento que este en el conjunto y lo queramos eliminar nos saltara un error

conjunto_paises.discard('col') #elimina un elemento del conjunto y si no lo encuentra solo lo descarta el pedaso de codigo y no pasa nada 
print(conjunto_paises)

conjunto_paises.clear() #limpia todo el conjunto 
print(conjunto_paises)
print(len(conjunto_paises))