litry = float(input("Ile litrów zużył samochód? "))
kilometry = float(input("Ile kilometrów przejechał? "))
cena = float(input("Ile kosztował litr paliwa? "))

zużycie = (litry*100) / kilometry
koszt1km = (cena * litry) / kilometry

print("Średnie zużycie paliwa:", zużycie, "l/100km")
print("Koszt jednego kilometra:", koszt1km, "zł")