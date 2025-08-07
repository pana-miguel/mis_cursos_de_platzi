import charts
import leer

def run():
    data = leer.leer('./proyecto/data2.csv')
    data = list(filter(lambda x: int(x['employees']) > 10000000, data))
    industry = list(map(lambda x: x['industry'], data))
    employees = list(map(lambda x: int(x['employees']), data))
    charts.generar_grafica_circulo(industry, employees)

if __name__ == '__main__':
    run()
