#Desempaquetado args
def add(a, b, c):
    return a + b + c

args = (1, 2, 3)
print(add(*args)) 

def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

kwargs = {"name": "Ana", "age": 28} 
show_info(**kwargs)