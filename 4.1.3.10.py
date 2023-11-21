## Dawid Janik IITiP/G 18.03 ZDM
def l100kmtompg(litry):  # Pierwszy kod
    galony = litry / 3.785411784
    mile = 100 * 1000 / 1609.344
    return mile / galony

def mpgtol100km(mile):  # Drugi kod
    km100 = mile * 1609.344 / 1000 / 100
    litry = 3.785411784
    return litry / km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))