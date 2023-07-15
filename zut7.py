from random import randint
numerki = []
ile = 6
max = 49
while len(numerki) < ile:
    numerek = randint(1,max)
    if numerek in numerki:  #jeśli wylosowana liczba jest już w liście, to program wylosuje nową wartość, żeby jej nie powielać w liście.
        continue
    numerki.append(numerek)
print(sorted(numerki))
