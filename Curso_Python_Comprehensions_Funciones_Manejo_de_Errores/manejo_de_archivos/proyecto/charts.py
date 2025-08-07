import matplotlib.pyplot as plt

def generar_grafica_barras(etiqueta, valor):
    fig, ax = plt.subplots()
    ax.bar(etiqueta, valor)
    plt.show()

def generar_grafica_circulo(etiqueta, valor):
    fig, ax = plt.subplots()
    ax.pie(valor, labels = etiqueta)
    ax.axis('equal')
    plt.show()

#ejemplo de uso sin importar un csv
if __name__ == '__main__':
    etiqueta = ['a', 'b', 'c']
    valor = [10, 40, 800]
    # generar_grafica_barras(etiquetas, valores)
    generar_grafica_circulo(etiqueta, valor)