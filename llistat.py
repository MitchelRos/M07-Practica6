areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12,
         "rebedor", 4.23]
# Imprimir el segon element
def imprimirSegon():
    print("Segons element {}".format(areas[1]))

def ultimElement():
    # El "len" es com fer "areas.lentgh" i resto 1, pero que de 0 al 13 (14 elements)
    print("Ultim element {}".format(areas[len(areas) - 1]))

def areaTerrasa():
    # Busca la posicio de la area
    posicioTerrasa = areas.index("terrassa")
    # En la posicio seguent es l"area
    posicioAreaTerrassa = posicioTerrasa + 1
    print("Area de la terrassa {}".format(areas[posicioAreaTerrassa]))

def elementPrimeriTercer():
    print("PrimerElement: '{0}' TercerElement: '{1}'".format(areas[0], areas[2]))

def elementTerceriUltim():
    print("TercerElement: '{0}' UltimElement: '{1}'".format(areas[2], areas[len(areas) - 1]))

def modificaLavabo():
    # Busca la posicio de la area
    posicioLavabo = areas.index("lavabo")
    # En la posicio seguent es l"area
    posicioAreaLavabo = posicioLavabo + 1
    areas[posicioAreaLavabo] = '666'
    #Imprimir la llista
    print(areas)

def totalAreaHabitacions():
    #Habitacio 1
    habitacio1 = areas.index("habitació1")
    posicioArea1 = habitacio1 + 1

    #Habitacio 2
    habitacio2 = areas.index("habitació2")
    posicioArea2 = habitacio2 + 1
    print('La suma de les habitacions es {}'.format((areas[posicioArea1]+areas[posicioArea2])))

def afegirPatiInterior():
    ##  Afegir l’area de “pati interior” i 2.78 a les últimes posicions
    patiInteriorName = 'pati interior'
    patiInteriorArea = 2.78
    #Afegeix el pati interior i la area
    areas.append(patiInteriorName)
    areas.append(patiInteriorArea)
    #Imprimir la llista
    print(areas)

#Crida totes les funcions
def callListat():
    #Imprimir el segon element
    imprimirSegon()
    #Imprimir l’últim element
    ultimElement()
    #Imprimir l’àrea de la terrassa
    areaTerrasa()
    #Imprimir del primer element al tercer element
    elementPrimeriTercer()
    #Imprimir del tercer element a l’últim
    elementTerceriUltim()
    #Imprimir el total de l’area de les dues habitacions
    totalAreaHabitacions()
    #Modificar l’àrea del lavabo i imprimir la nova list area
    modificaLavabo()
    #Afegir l’area de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area
    afegirPatiInterior()

#callListat()