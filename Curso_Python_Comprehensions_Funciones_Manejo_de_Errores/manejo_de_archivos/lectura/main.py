import leer_csv
import untils
import charts

def run():
    data = leer_csv.read_csv('./lectura/data.csv')

    country = input('Escribe el pais que quieres buscar: ')

    resultado = untils.population_by_country(data, country)

    if len(resultado) > 0:
        country = resultado[0]
        keys, values = untils.get_population(country)
        charts.generate_bar_chart(keys, values)

    print(resultado)

if __name__ == '__main__':
    run()   