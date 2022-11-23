#-----------------------------------------                                 #1                         
#Programm zur Umrechnung der Temerperatur
#von Grad Celsius in Grad Fahrenheit
#
#Autor: Frank Rudolph
#Datum: 16. November 2022
#-----------------------------------------
print("---------------------------------------------------")               #2
print("Umrechnung der Temperatur von Celsius in Fahrenheit")               #3
print("---------------------------------------------------")               #4
print()

Celsius = input("Bitte geben Sie eine Temperatur in Celsius ein: ")        #5
print(type(Celsius))

Celsius = float(Celsius)                                                   #6

print(type(Celsius))

Fahrenheit = 9/5 * Celsius + 32                                            #7

print()
print("Sie haben %2.f Grad Celsius eingegeben." % Celsius)                 #8
print()
print("Diese Temperatur entspricht %2.f Grad Fahrenheit." % Fahrenheit)    #9
                                        