conjunto1 = {'col','mex','bol'}
conjunto2 = {'pe','bol'}

conjunto3 = conjunto1.union(conjunto2) #une los dos conjuntos dejando solo un elemento de cada uno ya que bol se repite dos veces pero deja 1
print(conjunto3)

conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)

conjunto3 = conjunto1.difference(conjunto2)
print(conjunto3)

conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)