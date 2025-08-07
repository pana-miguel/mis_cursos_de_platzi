import matplotlib.pyplot 

def generar_grafica_barras(etiquetas, valores):
    fig, ax = matplotlib.pyplot.subplots()
    ax.bar(etiquetas, valores)
    matplotlib.pyplot.show()

def generar_grafica_circulo(etiquetas, valores):
    fig, ax = matplotlib.pyplot.subplots()
    ax.pie(valores, labels = etiquetas)
    ax.axis('equal')
    matplotlib.pyplot.show()

if __name__ == '__main__':
    etiquetas = ['a', 'b', 'c']
    valores = [10, 40, 800]
    # generar_grafica_barras(etiquetas, valores)
    generar_grafica_circulo(etiquetas, valores)
