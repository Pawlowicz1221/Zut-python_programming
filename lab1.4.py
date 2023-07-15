a = int(input("Podaj liczbę całkowitą: "))

if a % 2 == 0:
    print("Podana liczba jest liczbą całkowitą parzystą")
else:
    print("Podana liczba jest liczbą nieparzystą")

if not a % 2:
    print("parzysta")
else:
    print("nieparzysta")

if a & 1:
    print("nieparzysta")
else:
    print("parzysta")
# jeden w ifie każda wartość inna niż 0 daje wartość TRUE, a zero i wartość ujemna daje wartość FALSE
# "&" ten znak konwertuje podaną liczbę na system bitowy dwójkowy -> np. jeśli a to 5, wówczas w systemie dwójkowym ta wartość wyniesie 101
# 1 to 001, następnie dodajemy te liczby i jeśli wynik końcowy to +1 to mamy true. 0 & 0 = 0, 0 & 1 = 0, 1 & 0 = 0, 1 & 1 = 1