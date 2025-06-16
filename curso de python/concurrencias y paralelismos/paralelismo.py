import multiprocessing
import multiprocessing.pool

#uncion que calcule el cuadrado de un numero 
def calcular_numero(n):
    return n * n

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]

    with multiprocessing.Pool() as pool:
        resultado = pool.map(calcular_numero, numeros)

    print(f'resultados: {resultado}')




   
  
