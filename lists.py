newlist = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

for x in newlist:
    print(x.capitalize(), end=" ")
print()

list2 = list(range(-5, 20+1)) + list(range(10, 20))
reve = list(list2)
reve2 = list2.copy()
reve.sort(reverse=True)
reve2.sort(reverse=True)
list2.sort()

print(list2)
print(reve)
print(reve2)

print('list2 max: ', max(list2))
print('list2 min: ', min(list2))
print('list2 sum: ', sum(list2))

seg = list2[10: 15]
print(seg)