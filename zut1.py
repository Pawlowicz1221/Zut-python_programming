from math import sqrt
x = float(input("Wpisz liczbę: "))
while x < 0:
    x = float(input("Podaj liczbę dodatnią: "))
else:
    y = sqrt(x)
    print("pierwiastek wynosi:",y)