import csv
import numpy as np

plik = "meteo.csv"  # Wczyta, jeśli plik będzie w tej samej lokalizacji, co program (Jeśli nie, to zastosuj bezwzględną ścieżkę dostępu.)

lista = []

with open(plik, 'r') as plikcsv:
    csvreader = csv.reader(plikcsv)
    naglowek = next(csvreader)
    print(naglowek)

    for wiersz in csvreader:
        lista.append(wiersz)
        #print(wiersz)

#print(lista)
# Poza meritum
# with open(plik, 'r') as plikcsv:
#    csvreader = csv.reader(plikcsv)
#    naglowek = next(csvreader)
 
#   print(naglowek)
 #   licznik = 0
   # for wiersz in csvreader:
    #    lista.append(wiersz)
     #   licznik = licznik + 1
      #  print(licznik)

#print(lista)
 

# naglowek to lista
# next() - przeskoczył do kolejnego wiersza w iteratorze

# r - uprawnienia do czytania "read"

# Zadanie 1b)

print(naglowek)
print(lista) # Ma 5 elementów.


tablica = np.array(lista)
print(tablica)

# Jeśli nie działa numpy, to prawy dolny róg (nie miniConda, tylko base)
# Jakby co, ponowne uruchomienie.

#print(tablica[3])
# temp. kolumna 5
# wilgotność kolumna 8
# ciśnienie kolumna 10

print(tablica[0][4])

suma_temp = 0
suma_wilg = 0
suma_cisn = 0

for i in range(0,5):
       temperatura = float(tablica[i][4])
       wilgotnosc = float(tablica[i][-3])
       cisnienie = float(tablica[i][-1])
       #print(temperatura)
       suma_temp = suma_temp + temperatura
       suma_wilg = suma_wilg + wilgotnosc
       suma_cisn = suma_cisn + cisnienie
       #print(suma_temp)
       
srednia_1 = suma_temp / len(tablica)
print(srednia_1)
srednia_2 = suma_wilg / len(tablica)
print(srednia_2)
srednia_3 = suma_cisn / len(tablica)
print(srednia_3)




