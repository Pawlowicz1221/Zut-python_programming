lista = []
while len(lista) < 6:
    x = int(input("Podaj liczbę od 1 do 10: "))
    lista.append(x)
piątki = 0
for i in range(len(lista)):
    if lista[i] == 5:
        piątki += 1
print("Liczba piątek wynosi: ", piątki)

#wersja odporna na użytkownika:
ile = 0
loops = 0
while True:
    liczby = int(input("Podaj liczbę od 1 do 10: "))
    while liczby < 1 or liczby > 10:
        print("Złe liczby!")
        liczby = int(input("Podaj liczbę od 1 do 10: "))
    else:
        if liczby == 5:
            ile += 1
        loops += 1
        if loops == 6:
            break
print("Użytkownik wybrał liczbę '5'", ile, "razy.")
