a = [1,2,3,4,5]
b = a
print(a)
print(b)    

del a[0] #elimina el primer elemento de la lista a
print(a)
print(b) #la lista b se ve afectada porque apunta a la misma lista que a

print(id(a)) #muestra la dirección de memoria de a
print(id(b)) #muestra la dirección de memoria de b  

c = a[:] #esto crea una copia de la lista a en c
print(id(c)) #muestra la dirección de memoria de c

a.append(6) #agrega el 6 a la lista a
print(a) #muestra la lista a        
print(b) #muestra la lista b
print(c) #muestra la lista c ya nos e modicifa la informacion de c porque es una copia de a y no apunta a la misma dirección de memoria que a y b

