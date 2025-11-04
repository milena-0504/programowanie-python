wiek = input("Podaj wiek studenta: ")
wiek = int(wiek)

plik = open("wiek_drugiego_studenta.txt")
tresc = plik.read()
print(tresc)

x = int(tresc)
#print(x)

diff = x-wiek

if wiek < x:
    zmienna = "Pierwszy student jest młodszy od studenta drugiego o " + str(diff) + " " +"lata."
    print(zmienna)


# Zapis do pliku

with open ("wiek_2.txt", 'a') as plik:
    plik.write(zmienna)