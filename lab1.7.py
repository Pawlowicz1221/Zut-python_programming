a = [1,2,3]
b = ['a','b','c']
for x in a:
    for y in b:
        print(x,y)

for x in range(1,4):
    for y in 'abc':
        print(x,y)
#for y in 'abc': - Ta linia definiuje drugą pętlę for, która iteruje po znakach w ciągu znaków 'abc'. Zmienna y przyjmuje kolejne wartości 'a', 'b' i 'c'.

#trzeci sposób to po prostu ręczne wypisanie wszystkich wartości w princie