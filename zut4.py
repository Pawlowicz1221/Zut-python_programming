#program liczący największą z podanych liczb
a = 1
max = -9999999999999999999999999999999999999999999999999999
while a != 0:
    a = int(input("Podaj liczbę, albo 0 aby zakończyć: "))
    if a > max:
        max = a
print("Największa liczba to: ", max)

#wariant ze strażnikiem:
#    max = -999999999
#    a = 1
#    licz = 0
#    while a != 0:
#       a = int(input(“Podaj liczbę albo 0 aby zakończyć: "))
#       if a != 0:
#           if a > max:
#               max = a
#           licz = licz + 1
#    if licz > 0:
#       print("Największa liczba to ", max)
#    else:
#       print("Nie podałeś żadnych liczb :( ")
