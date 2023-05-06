
print("KORTRÄKNARE")

#Skapar kortleken
färger = ["Hjärter", "Ruter", "Klöver", "Spader"]
valörer = ["Äss", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"]
kortlek = []
for valör in valörer:
    for färg in färger:
        kort = f"{färg} {valör}"
        kortlek.append(kort)

dealerSumma = 0
antalSpelare = input('Hur många spelare spelar?\n> ')

#Medan du spelar
while 10 > 0:
    spelatKort = input('vilket kort har spelats?\n> ')

    while 1 < 2:
        if spelatKort in kortlek:
            kortlek.remove(spelatKort)
            break
        else:
            spelatKort = input('Vänligen skriv ett fungernade kort\n>')
    
    #Dealeromgång
    if dealerSumma < 16:
        spelatKort = input('vilket kort drog dealern?\n> ')
        #LÄGG TILL NY BERÄKNING AV DEALER SUMMA; BUGG
    else:
        print('Dealern har stannat')


print(kortlek)

#Kolla vilket kort det givna är
def kortKollare(kort):
    splittad = [x.split() for x in kort.split(' ')]
    if splittad[1] == 'Äss':
        return 1
    elif splittad[1] == 'Knäckt' or splittad[1] == 'Dam' or splittad[1] == 'Kung':
        return 10
    else:
        return splittad[1]
