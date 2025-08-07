import leer_csv
import charts

def run():
    data = leer_csv.read_csv('./lectura/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data)) #aqui se filtran solo los paises de asia 
    country = list(map(lambda x: x['Country/Territory'], data))
    porcentajes = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(country, porcentajes)

if __name__ == '__main__':
    run()   