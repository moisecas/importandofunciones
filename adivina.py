import random


def violeta():
    numero_aleatorio = random.randint(1, 100) 
    numero_elegido = int(input("elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("digita un numero mas grande")
        else: 
             print("digita un numero mas pequeño")
        numero_elegido=int(input("elige otro numero: "))
    print("ganaste") 


if __name__== "__main__":
    violeta() 