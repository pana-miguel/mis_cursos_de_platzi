class cuenta():                               #definicion de la clase cuenta
    def __init__(self, cuenta, balance):      #definimos el constructor de la clase con las variables cuenta y balance
        self.cuenta = cuenta                  #inicializamos la variable cuenta con el valor de cuenta que es el nombre de la cuenta
        self.balance =balance                 #inicializamos la variable balance con el valor de balance que es el saldo de la cuenta
        self.cuenta_activa = True             #inicializamos la variable cuenta_activa en True para indicar que la cuenta esta activa

    def depositar(self, cantidad):            #definimos el metodo depositar que recibe una cantidad
        if self.cuenta_activa:                #verificamos si la cuenta esta activa
            self.balance += cantidad          #sumamos la cantidad al balance con el operador += que es una forma de asignar el resultado de la suma a la variable balance
            print(f"Se han depositado {cantidad} a la cuenta {self.cuenta}.")  #imprimimos el mensaje de que se ha depositado la cantidad a la cuenta
        else:
            print("La cuenta no esta activa.")  #imprimimos el mensaje de que la cuenta no esta activa si es el caso

    def retirar(self, cantidadRtiro):
        if self.cuenta_activa:
            if cantidadRtiro <= self.balance:
                self.balance -= cantidadRtiro
                print(f"Se han retirado {cantidadRtiro} de la cuenta {self.cuenta}. saldo actual: {self.balance}")

    def desactivar_cuenta(self):               #definimos el metodo desactivar_cuenta
        self.cuenta_activa = False             #cambiamos el valor de cuenta_activa a False para indicar que la cuenta no esta activa
        print(f"La cuenta {self.cuenta} ha sido desactivada.") #imprimimos el mensaje de que la cuenta ha sido desactivada

    def activar_cuenta(self):
        self.cuenta_activa = True
        print(f"La cuenta {self.cuenta} ha sido activada.")
    
cuenta1 = cuenta("miguel", 1000) #definimos la cuenta1 con el nombre de la cuenta y el saldo
cuenta2 = cuenta("jose", 5000)   #definimos la cuenta2 con el nombre de la cuenta y el saldo

#llamado a los metodos
cuenta1.depositar(500)           #llamamos al metodo depositar de la cuenta1 con la cantidad de 500
cuenta2.depositar(200)           #llamamos al metodo depositar de la cuenta2 con la cantidad de 200
cuenta1.desactivar_cuenta()      #llamamos al metodo desactivar_cuenta de la cuenta1
cuenta1.depositar(200)           #llamamos al metodo depositar de la cuenta1 con la cantidad de 200 pero no se depositara porque la cuenta no esta activa
cuenta1.activar_cuenta()         #llamamos al metodo activar_cuenta de la cuenta1
cuenta1.depositar(200)           #llamamos al metodo depositar de la cuenta1 con la cantidad de 200 y ahora si se depositara porque la cuenta esta activa
