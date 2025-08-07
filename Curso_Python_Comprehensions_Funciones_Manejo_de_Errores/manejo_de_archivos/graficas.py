import matplotlib.pyplot as plt

def grafica(labels, valores):
    fig, ax = plt.subplots()
    ax.bar(labels, valores)
    plt.show()

def grafica_torta(labels, valores):
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels,)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['A','B','C']
    valores = [100, 200, 300]
    #grafica(labels, valores)
    grafica_torta(labels, valores)