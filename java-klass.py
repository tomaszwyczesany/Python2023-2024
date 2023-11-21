import z3

def main():
    s = z3.Solver()
    c = [z3.BitVec(str(i), 8) for i in range(12)]
    s.add(c[0] == ord('N'))
    s.add(c[5] < ord('b'))
    s.add(c[6] == c[0] - 3)
    s.add(c[10] == c[6] + (c[11] / 11) * 3)
    s.add(c[7] == c[4] + 1)
    s.add(c[1] == c[0] + 27)
    s.add(c[2] > c[1] + 1)
    s.add(c[3] == c[1])
    s.add(c[4] == c[1] + (c[0] - 1) / 7)
    s.add(c[5] > ord('`'))
    s.add(c[8] == c[7] - 3)
    s.add(c[9] == c[4])
    s.add(c[11] > c[0] + 31)
    print(s.check())
    print(s.model())
    print(''.join([chr(s.model()[x].as_long()) for x in c]))
    pass

main()