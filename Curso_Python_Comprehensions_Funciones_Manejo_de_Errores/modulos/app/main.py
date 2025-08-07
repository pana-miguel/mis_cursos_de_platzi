import mod 

informacion = [
    {
        'pais': 'Colombia',
        'Population': 500
    },
    {
        'pais': 'Bolivia',
        'Population': 300
    }
    ]

def run():
    llaves, valores = mod.get_poblacion()
    print(llaves, valores)

    resultado = mod.poblacion_pais(informacion, 'Colombia')
    print(resultado)

#este if es para que no se ejecute el main si se importa desde otro archivo y solo se puede ejecutar en este 
if __name__ == '__main__':
    run()
