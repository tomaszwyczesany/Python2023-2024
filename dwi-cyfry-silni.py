ile_p = int(input())
for i in range(ile_p):
    n = int(input())
    if n == 0 or n == 1:
        print("0 1")
    elif n == 2:
        print("0 2")
    elif n == 3:
        print("0 6")
    elif n == 4:
        print("2 4")
    elif n == 5 or n == 6 or n == 8:
        print("2 0")
    elif n == 7:
        print("4 0")
    elif n == 9:
        print("8 0")
    else:
        print("0 0")
