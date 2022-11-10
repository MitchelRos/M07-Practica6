
import random

def adivinaEdat():
    #Busca un numero al atzar de 1 al 50
    edat = random.randint(1,50)
    #Pregunta per primer cop
    adivina = int(input("Adivina l'edat entre 1 i 50"))

    #Si no es igual el numero escrit a el numero segueix el bucle
    while(edat != adivina):
        #Pregunta un altre cop es es pasa del numero
        if edat<adivina:
            adivina = int(input("L'edat es menor"))
        #Pregunta un altre cop es es queda curt del numero
        elif(edat>adivina):
            adivina = int(input("L'edat es major"))

    #Al sortir del bucle ho ha adivinat
    print("Correcte, l'edat era {}".format(adivina))

adivinaEdat()
