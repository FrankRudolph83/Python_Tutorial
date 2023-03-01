#-------------------------------------------------------------
# Globale und lokale Variablen im Kontext von Funktionen
#
#Autor:   Dein Name
#Datum:   Aktuelles Datum
#-------------------------------------------------------------


# Überschreiben der Variablen "zahl"
def zahl_ersetzen():
zahl = 20
    print("Funktion: Neuer Wert:", zahl)
    testvariable = 408
    print("Testvariable:", testvariable)


# Hauptprogramm
zahl = 17

zahl_ersetzen()
print("Hauptprogramm: Neuer Wert:", zahl)

# Das wäre ein Fehler!
#print("Testvariable:", testvariable)