list_one = [100, 5, 90, 15, 80, 25, 70, 35, 60, 45, 50, 55, 40, 65, 30, 75, 20, 85, 10, 95]
print("list_one =", list_one)


def bubble_sort(mylist):
    a = 0
    last_item = len(mylist) - 1
    print("last_item =", last_item)
    for z in range(0, last_item):
        print('z =', z)
        for x in range(0, last_item - z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
            a = a + 1
            print(f"iter.№ {a}:", list_one)
    return mylist


newlist = bubble_sort(list_one).copy()
print("mewlist =", newlist)
print(newlist)