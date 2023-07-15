from time import sleep
czas = float(input("Podaj czas do odliczenia: "))
while czas >= 0:
    print(czas, "...")
    czas -= 1
    sleep(1)
print("Gratulacje!")

# druga wersja zmuszająca użytkownika do wprowadzenia dobrych danych
from time import sleep
czas = 0
while czas <= 0:
    czas = int(input("Ile czasu odliczyć? "))
    if czas <= 0:
        print("Podaj dodatnią lcizbę! ")
while czas >= 0:
    print("...", czas)
    czas -= 1
    sleep(1)
print("Odliczanie zakończone!")