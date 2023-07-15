#program który wybierze największą z 4 liczb
a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
c = int(input("Podaj liczbę: "))
d = int(input("Podaj liczbę: "))
max = a
if b > max:
    b = max
if c > max:
    max = c
if d > max:
    max = d
print("Największa liczba to: ", max)