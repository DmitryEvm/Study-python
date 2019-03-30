pr = input("что вывести: ")
a = int(input("сколько раз вывести: "))
n = 0
for z in range(a):
    n += 1
    print(f'iter.#{n}: ', end="")
    print(pr)
    a -= 1

print('end')