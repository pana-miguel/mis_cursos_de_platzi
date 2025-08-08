import store
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4]


@app.get("/contact")
def get_list():
    return {'name' : "FastAPI" , 'version' : "0.1.0"}


def run():
    store.get_categories() #trae todas las categorias de la tienda 

if __name__ == "__main__":
    run()