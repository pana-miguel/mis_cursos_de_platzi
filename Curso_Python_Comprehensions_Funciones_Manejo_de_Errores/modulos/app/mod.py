def get_poblacion():
    llaves = ['col', 'bol']
    valores = [300, 400]
    return llaves, valores 

def poblacion_pais(informacion, pais):
    resultado = list(filter(lambda x: x['pais'] == pais, informacion))
    return resultado
 