
#Inici una funcio
def estalviar():
    dinersInicials = 100
    sumaDiners = 0
    anys = 7
    increment = 1.1
    # Bucle del 1 al 7
    for x in range(anys):
        # Suma els diners durant 7 anys
        sumaDiners = (sumaDiners + dinersInicials) + increment

    # Imprimir el total dels diners acumulats després de 7 anys
    print('Diners inicials: {}'.format(dinersInicials))
    print('La suma de diners es {}'.format(sumaDiners))

#Crida la funcio
#estalviar()