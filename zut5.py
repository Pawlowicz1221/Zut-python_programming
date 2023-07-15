#zastosowanie komendy "break" aby wyjść z pętli wcześniej
max = -999999999
licz = 0
while True:
    a = int(input("Podaj liczbę albo 0 aby zakończyć: "))
    if a == 0:
        break
    if a > max:
        max = a
    licz = licz + 1
if licz > 0:
    print("Największa liczba to ", max)
else:
    print("Nie podałeś żadnych liczb :( ")
