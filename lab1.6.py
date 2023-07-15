a = [9,7,5,3,1]
a.reverse()
for x in a:
    print(x, end=" ")

print()
a=11
for i in range(5):
    a = a - 2
    print(a, end=" ")

print()
for a in range(9,0,-2):
    print(a, end=" ")
#for a in range(9,0,-2):: Ta linia definiuje pętlę for, która iteruje po wartościach zmiennej a. Funkcja range(9, 0, -2) tworzy sekwencję wartości od 9 do 0 (włącznie), z krokiem -2. Oznacza to, że wartość a będzie przyjmować kolejno wartości 9, 7, 5, 3, 1.

print()
x = [9, 7, 5, 3, 1]
for y in range(len(x)):
    print(x[y], end=' ')

print()
x = [9, 7, 5, 3, 1]
for y in (x):
    print(y, end=' ')