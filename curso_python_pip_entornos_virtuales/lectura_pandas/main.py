import untils
import leer_csv
import charts
import pandas as pd 

def run():
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']  # Filtrar solo los paises de America del Sur

    paises = df['Country/Territory'].values # Obtener los nombres de los paises
    porcentajes = df['World Population Percentage'].values # Obtener los porcentajes de la poblacion
    charts.generate_pie_chart(paises, porcentajes)

    pais = input('Ingrese el nombre del pais: ')
    print(pais)
    data = leer_csv.read_csv('data.csv')
    resultado = untils.population_by_country(data, pais)



if __name__ == '__main__':
    run()   