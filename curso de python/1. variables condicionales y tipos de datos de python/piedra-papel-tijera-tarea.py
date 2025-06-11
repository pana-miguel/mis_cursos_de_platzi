jugador1 = input("Jugador 1, ingrese su nombre: ") 
jugador2 = input("Jugador 2, ingrese su nombre: ")

jugador1_eleccion = input(f"{jugador1}, elija piedra, papel o tijera: ")
jugador2_eleccion = input(f"{jugador2}, elija piedra, papel o tijera: ")

if jugador1_eleccion == jugador2_eleccion:
    print("Es un empate!")
elif jugador1_eleccion == "piedra" and jugador2_eleccion == "papel":
    print(f"{jugador2} gana!")
elif jugador1_eleccion == "papel" and jugador2_eleccion == "tijera":    
    print(f"{jugador2} gana!")
elif jugador1_eleccion == "tijera" and jugador2_eleccion == "piedra":
    print(f"{jugador2} gana!")
elif jugador1_eleccion == "papel" and jugador2_eleccion == "piedra":
    print(f"{jugador1} gana!")
elif jugador1_eleccion == "tijera" and jugador2_eleccion == "papel":
    print(f"{jugador1} gana!")
elif jugador1_eleccion == "piedra" and jugador2_eleccion == "tijera":
    print(f"{jugador1} gana!")
else:
    print("Elección inválida. Por favor, elija entre piedra, papel o tijera.")

    

