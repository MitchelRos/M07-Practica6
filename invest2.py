#Funcio invest per saber la quantitat de diners
def invest2():
    #Fiquem les variables per la quantitat de diners
    #Fiquem quantitat inicial
    diners_inicials=100
    #Guardem la quantitat del diners_inicials
    savings = diners_inicials
    #Augmenta aquesta quantitat durant la vairable anys
    increase = 1.1
    #Li fiquem els anys que obte els diners
    anys = 7

    #Fem el bucle per la quantitat de diners que tenim, agafem els numero d'anys i entre el numero d'anys es calcula els diners_inicials i els savings
    for i in range(anys):
        #Agafem els diners inicials y es suma +1 en la variable
        diners_inicials += 1
        #afegim els savings i ho fiquem amb els diners inicials
        savings += diners_inicials

    #i en resultat ens mostra quants diners tenim durant els

    result = savings

    #Es mostra el resultat final
    print(result)

#invest2()







