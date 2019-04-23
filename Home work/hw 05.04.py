import random

num = []
for i in range(3):
    num.append(random.randint(1, 4))
print(num)
dub = 0
num.sort()
for i in range(len(num)-1):
    if num[i] == num[i+1]:
        dub += 1
if dub != 0:
    print('doubles: yes:', dub)
else:
    print('doubles: no')
print('---')
print(num)
sum4 = 0
if num[0] + num[1] == 4:
        sum4 += 1
if num[0] + num[2] == 4:
        sum4 += 1
if num[1] + num[2] == 4:
        sum4 += 1
if sum4 != 0:
    print('sum = 4: yes:', sum4)
else:
    print('sum = 4: no')
print('---')

sum_num2 = 0
num2 = [i for i in range(14+1)]
print(num2)
for i in range(len(num2)):
    sum_num2 += num2[i]

sum_num3 = sum(num2)
print(sum_num2)
print(sum_num3)
print('---')

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for i in range(len(days)):
    if i < 5:
        print(i+1, days[i], '- weekday')
    else:
        print(i+1, days[i], '- weekend')
print('---')

for i, n in enumerate(days, 1):
    if i < 6:
        print(i, n, '- weekday')
    else:
        print(i, n, '- weekend')
print('---')