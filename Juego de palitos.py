from random import *
#lista inicial
palitos = ["-", "--", "---", "----"]


#Mezclar palitos
def mezcla(lista):
    shuffle(lista)
    return lista


#Validar que usuario ingrese un numero valido
def palitos_aleatorio():
    valor_usuario = ""
    while valor_usuario not in ["1", "2", "3", "4"]:
        valor_usuario = input(" Escoge un numero del 1 al 4:  ")
    return valor_usuario


#comprobacion de intento
def turno(valor_usuario):

    valor_usuario_int = (int(valor_usuario))-1
    turnox = palitos[valor_usuario_int]
    if palitos[valor_usuario_int] == "-":
        print(f"\nLaaaaastima Margaritoooo, perdiste \n has sacado  {turnox}")
    else:
        print(f"\nAfortunado que sos, \n  has sacado el {turnox}")
    return valor_usuario_int


cuenta = 20
while cuenta > 1:
    print(f"Actualmente tenemos {palitos}  \n mucha suetrte!!! ")

    valor_usr = palitos_aleatorio()
    mezcla(palitos)
    palitos.pop(turno(valor_usr))

    cuenta = len(palitos)
