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
    if num[i] + num[i+1] == 4:
        print('yes! 4')
    if i == range(len(num)):
        break
if dub != 0:
    print('yes')
else:
    print('error')

sum_num2 = 0
num2 = [i for i in range(14+1)]
print(num2)
for i in range(len(num2)):
    sum_num2 += num2[i]

sum_num3 = sum(num2)
print(sum_num2)
print(sum_num3)
