import random
import hashlib
main_int = [0x6e, 0x6f, 0x4d, 0x72, 0x2e, 0x54, 0x72, 0x6f, 0x6c, 0x6f, 0x6c, 0x6f, 0x20]
print(main_int)
ma = '\x4b\x68'
print(ma)
key1 = random.randint(1, 10) * 4 % 9000
print(key1)
ar = '\x45\x64'
print(ar)
overkill = []
frogs = [0x65, 0x61, 0x73, 0x72, 0x64, 0x21]
print(frogs)
ey = '\x75\x61'
print(ey)
mad = 'u'
over_9000 = []
ou = '\x72\x64'
print(ou)
base = key1 * 64
print(base)
d = '\x69\x6c'
print(d)
me = hashlib.md5()
print(me)
for pepe in main_int:
    pepe += 2 ^ 2
    over_9000.append(pepe)
    print(over_9000)
print(over_9000)
over_kill = over_9000[8:-1]
print("over kill ",over_kill)
print(str("".join([chr(rage) for rage in over_kill])))