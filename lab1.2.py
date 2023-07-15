diskSize = 140
diskSizeUsed = 100
fileSize = float(input("Wielkość pliku w GB: "))
freeSpace = (diskSize - diskSizeUsed)

if freeSpace >= fileSize:
    print("Pobranie pliku zakończone sukcesem")
else:
    print("Brak miejsca na dysku")