def czy_przestepny(rok):
	if rok % 4 != 0:
		return False
	elif rok % 100 != 0:
		return True
	elif rok % 400 != 0:
		return False
	else:
		return True
def dni_w_miesiacu(rok, miesiac):
	if rok < 1582 or miesiac < 1 or miesiac > 12:
		return None
	dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	wyn = dni[miesiac - 1]
	if miesiac == 2 and czy_przestepny(rok):
		wyn = 29
	return wyn

testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [ 2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	print(wynik)

