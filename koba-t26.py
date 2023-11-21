# zadanie połączyć 2 pliki i zapisać do trzeciego
plik1 = str(input("podaj nazwe pierwszego pliku"))
plik2 = str(input("podaj nazwe drugiego pliku"))
plik3 = str(input("podaj nazwe trzeciego pliku"))
# otwarcie plików
file1 = open(plik1,"w")
file2 = open(plik2,"w")
file3 = open(plik3,"w")
# # zapis wszystkich lini pliku do zmiennej
dane1 = file1.write("CZesc")
dane2 = file2.write("Elo")

file1 = open(plik1,"r")
file2 = open(plik2,"r")

# odczyt z pliku
dane11 = file1.read()
dane22 = file2.read()

dane11 += "\n"
dane11 += dane22

file3.write(dane11)
# # zamkniecie plików
file1.close()
file2.close()
file3.close()
