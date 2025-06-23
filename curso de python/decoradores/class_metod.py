class contador():
    contador = 0

    #con el classmetodh se pueden usar objetos o variables externas a la funcion para modificarlas o simplemente implementarlas y usarlas
    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1

contador.incrementar_contador()
contador.incrementar_contador()
print(contador.contador)