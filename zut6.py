x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
szukana = float(input("Jakiej wartości szukamy? "))
a = False
for i in range(len(x)):
    if x[i] == szukana:
        a = True
        break
if a is True:           #można po prostu zapisać to jako 'if a', co oznacza w skrócie: if a is true
    print("Dana znajduje się na miejscu ", i)
else:
    print("Nie ma takiej danej w liście.")
