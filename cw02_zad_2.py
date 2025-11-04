wiek = input("Podaj wiek studenta: ")
wiek = int(wiek)

plik = open("wiek_drugiego_studenta.txt")
tresc = plik.read()
print(tresc)

x = int(tresc)
print(x)

diff = x-wiek
print(diff)

if wiek < x:
    zmienna = "Pierwszy student jest mlodszy od studenta drugiego o " + str(diff) + " " +"lat(a)."
    print(zmienna)
else:
    zmienna_2 = "Pierwszy student jest starszy od drugiego o " + str(abs(diff)) + " " + "lat(a)."
    print(zmienna_2)


# Zapis do pliku

with open ("wiek_2.txt", 'a') as plik:
    plik.write(zmienna_2)