from operator import truediv
import random 

numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el numero")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un numero del 1 al 100: ")
    numero = int(entrada) #hice casteo porque el input es un string y necesito un numero
    
    if numero == numero_secreto:
        print("Adivinaste el numero")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:    
        print("El numero es menor al ingresado")
    
    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("Perdiste, se terminaron los intentos")