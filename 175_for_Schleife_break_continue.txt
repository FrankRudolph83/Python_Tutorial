#-------------------------------------------------------------
# for-Schleife mit break und continue
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

Endwert = int(input("Iterierung abbrechen bei: "))
Luecke = int(input("Geben Sie eine Lücke der Iterierung (Zahl) an: "))

for i in range(15):
    if i == Endwert:
        break

    if i == Luecke:
        print("Iterierung wird ausgelassen.")
        continue

    print("Iterierung: ", i)

print("Iterierung beendet")