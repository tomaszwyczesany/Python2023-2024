def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

li = []
for i in range(35):
    li.append(i)

print(li)
print(list_updater(li))