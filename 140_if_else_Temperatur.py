#-------------------------------------------------------------
# Die if-else-Bedingung
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------

# Temperaturwerte
ideale_temperatur = 28
minimal = 22
maximal = 32

# Aktuelle Temperatur ermitteln und auswerten
aktuelle_temperatur = int(input("Aktuelle Temperatur: "))

if aktuelle_temperatur == ideale_temperatur:
    print("Wohlfühltemperatur!")
    print("So kann es bleiben.")
else:
    print("Temperatur ist nicht ideal, Nachregelung starten")

    if aktuelle_temperatur < minimal:
    print("Achtung, es ist zu kalt!")
    print("Heizung wird eingeschaltet")
    else:
    print("Achtung, es ist zu warm!")
    print("Heizung wird ausgeschaltet")