while True:
    a = str(input("Proszę wcisnąć c, lub n: "))
    if (a == "n" or a == "c"):
        print("Dziękuję!")
        break
    else:
        print("zła litera")