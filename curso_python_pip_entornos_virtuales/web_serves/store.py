import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #significa el estado en el que se encuentra la peticion
    print(r.text) #imprime el contenido de la respuesta
    categorias = r.json() #convierte el contenido de la respuesta a un objeto de python

    for categoria in categorias:
        print(categoria['name'])


