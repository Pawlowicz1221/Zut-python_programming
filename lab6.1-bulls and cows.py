from random import randint

r = str(randint(1000, 9999))

print("Witamy w grze Cows and Bulls!")
while True:
    guess = input("Wprowadź swoją liczbę lub wytypuj 'exit' aby zakończyć: ")
    if guess == "exit":
        print("Zakończyłeś grę :(")
        break
    else:
        cows=0
        bulls=0
        if len(guess)!=4:
            continue
        for x in range(4):
            if guess[x]==r[x]:
                cows=cows+1
            elif guess[x] in r:
                bulls=bulls+1
        if guess==r:
            print("Gratulacje. Wygrałeś!")
            break
        print(cows," cows,",bulls," bulls")


