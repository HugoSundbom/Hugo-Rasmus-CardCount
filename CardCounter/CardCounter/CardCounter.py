
print("KORTRÄKNARE")
färger = ["Hjärter", "Ruter", "Klöver", "Spader"]
valörer = ["Äss", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"]
kortlek = []

for valör in valörer:
    for färg in färger:
        kort = f"{färg} {valör}"
        kortlek.append(kort)
spelat_kort = input('vilket kort har spelats?\n')
print(spelat_kort)
listLength = len(kortlek)
while 1 < 2:
    if spelat_kort in kortlek:
        kortlek.remove(spelat_kort)
        exit
    else:
        spelat_kort = input("Vänligen skriv ett fungernade kort ")


print(kortlek)
