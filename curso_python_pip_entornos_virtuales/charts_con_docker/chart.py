import matplotlib.pyplot as plt

def generar_grafico():
    labels = ['A', 'B', 'C', 'D']
    valores = [10, 20, 30, 40]

    fig, ax = plt.subplots() 
    ax.pie(valores, labels=labels)
    plt.savefig('grafico_nuevo.png')
    plt.close(fig)
    print("Gráfico guardado como 'grafico.png'")
