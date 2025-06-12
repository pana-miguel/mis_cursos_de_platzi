#Aplicación de Matrices
#Las matrices son una herramienta fundamental en muchas áreas de la computación y las matemáticas. En Python, podemos usar listas dentro de listas
#para representar matrices bidimensionales (2D). Hoy, vamos a explorar varias aplicaciones prácticas de las matrices y cómo estas estructuras pueden ser usadas para representar tableros de juego.

#Representación de Tableros de Juego
#Las matrices son ideales para representar tableros de juego en programación, como tableros de ajedrez, damas y otros juegos de mesa. Usar matrices
#para estos fines permite manejar fácilmente la disposición de las piezas y las reglas del juego.

#Ejemplo: Tablero de Ajedrez
#Un tablero de ajedrez es una matriz de 8x8. En vez de representar solo las casillas blancas y negras, podemos representar las piezas de ajedrez.
#Usaremos letras para representar las piezas: P para peón, R para torre, N para caballo (knight), B para alfil, Q para reina y K para rey. 
#Las piezas negras se representan con letras minúsculas y las blancas con letras mayúsculas.

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)  # Imprime el tablero de ajedrez
print("Caballo en la posicion [7][1]:", chess_board[7][1])  # Imprime la posición del caballo

chess_board[7][1] = 0  # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N'  # Nueva posición del caballo

print(chess_board)  # Imprime el tablero de ajedrez después de mover el caballo