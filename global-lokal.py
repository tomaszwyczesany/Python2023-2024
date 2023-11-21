a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)


a = 1
print(a)