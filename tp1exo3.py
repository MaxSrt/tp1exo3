jour = int(input("Entrez le nombre de jours : "))
heure = int(input("Entrez le nombre d'heures : "))
minute = int(input("Entrez le nombre de minutes : "))
j = jour*1440
h = heure*60
m = j+h+minute
print("Le nombre de minutes écoulés est de", m)

