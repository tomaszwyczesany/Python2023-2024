

# zadanie 3.1.1.11
napis = input("Podaj tekst : ")
if napis  == "Skrzydłokwiat":
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")
else:
    print("Nie, ja chcę Skrzydłokwiat...!")

# zadanie 3.1.1.12
dochód = float(input("Wprowadź roczny dochód: "))
podatek = 0.0
if dochód <= 85528:  // sprawdzam pierwszy warunek, Próg dochodowy do 85528
    podatek = dochód * 0.18 - 556.02 // obliczam podatek
    if podatek <= 0: // sprawdzamy czy kraj ma oddac podatek, jezeli tak
        podatek = 0  //  .... to nie zwracamy
else:
    podatek = 14836.02 + (dochód-85528) * 0.32 // w przeciwnym wypadku drugi próg dochodowy powyzej 85528


podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)


# zadanie 3.1.1.13

rok = int(input("Wprowadź rok: "))

if rok <= 1581:
    print("Nie w kalendarzu gregoriańskim")
elif rok % 4 != 0:
    print("Zwykły rok")
elif rok % 100 != 0:
    print("Rok przestepny")
elif rok % 400 != 0:
    print("Zwykły rok")
else:
    print("Rok przestępny")
