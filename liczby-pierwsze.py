def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return print("NIE")
    return print("TAK")

print(czy_pierwsza(12))
print(czy_pierwsza(13))