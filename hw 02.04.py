one = 'STRING'
print(f'1. The third char. in "{one}", is:', one[2])
print(f'2. The penultimate char. in "{one}", is:', one[-2])
print(f'3. First five char. in "{one}", is:', one[0:5])
print(f'4. "{one}" except two last char.:', one[0:-2])
print(f'5. Even char. in "{one}", is:', one[::2])
print(f'6. Even char. starting from the first in "{one}", is:', one[1::2])
print(f'7. "{one}" in reverse order:', one[::-1])
print(f'8. Char. in "{one}" in reverse order through one:', one[::-2])
print(f'9. String length "{one}", is:', len(one))
print('---')

number_list = [44, 4, 57, 10, 31, 23, 8]
print('number list =', number_list)
print('min =', min(number_list))
print('max =', max(number_list))
print('---')

x = 10
alter = []
for n in range(x):
    if n % 2 == 0:
        alter.append(0)
    else:
        alter.append(1)
print(alter)
print('---')

list_one = []
for n in range(x):
    if n == x-1 or n == 0:
        list_one.append(1)
    else:
        list_one.append(0)
print(list_one)
print('---')

list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8, 8, 8]
print(list_two)
counter = {}
for el in list_two:
    counter[el] = counter.get(el, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}
print(doubles)
print('---')

a = '_SOMETHING'
b = int(len(a))
c = int((b - 4) / 2)
d = c + 4
print(a[c:d])
