import charts
import leer

def run():
    data = leer.leer('./prueba1/data1.csv')
    deporte = list(map(lambda x: x['sport'], data))
    numero_atletas = list(map(lambda x: int(x['number of athletes']), data))
    charts.generar_grafica_circulo(deporte, numero_atletas)

if __name__ == '__main__':
    run()
