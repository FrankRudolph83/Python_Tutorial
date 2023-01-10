#-------------------------------------------------------------
# while-Schleife
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Menü ausgeben
print("Menü:")
print("1: Motor ein\n2: Motor aus")
print("3: Programm beenden")

aktion = 0

# Gewünschte Aktion abfragen
while aktion != 3:
    aktion = int(input("Aktion wählen: "))

    # Funktion ausführen
    if aktion == 1:
        print("Motor wird eingeschaltet")
    elif aktion == 2:
        print("Motor wird ausgeschaltet")
    elif aktion == 3:
        print("Programm wird beendet.")
    else:
        print("Ungültige Eingabe")