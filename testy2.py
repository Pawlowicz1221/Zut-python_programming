lista = [100, 2, 1, 4]
iloraz = lista[0]
for el in lista[1:]:
    iloraz /= el
print(iloraz)
nowalista = lista
print(nowalista)
lista[1] = 6
print(lista)
print(nowalista)
print(lista[-1])
lista.reverse()
print(lista)
print(lista.pop(0))
print(lista)
lista.extend(nowalista)
print(lista)
print(lista.count(6))