x = 5 #variable global

def cambiar_global():
    global x #se usa la palabra reservada global para definir la variable que queremos cambiar o usar 
    x+3 
    print(f"valor modificado {x}")

cambiar_global()
print(x)          #sigue estando el mismo valor porque se modifico de manera global