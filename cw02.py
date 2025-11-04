wiek_1 = input("Podaj wiek studenta nr 1: ")
wiek_2 = input("Podaj wiek studenta nr 2: ")

wiek_1 = int(wiek_1)
wiek_2 = int(wiek_2)

if wiek_1 > wiek_2:
   print("Pierwszy student jest starszy i ma", wiek_1, "lata.")

moj_tekst = "Pierwszy student jest starszy i ma " + str(wiek_1) + " " + "lata."
print(moj_tekst)

# Zapis do pliku

with open ("moj_plik.txt", 'a') as plik:
    plik.write(moj_tekst)