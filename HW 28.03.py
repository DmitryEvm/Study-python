a = 33
b = 17

print("1.")
print(f'a={a}, b={b}')
print('swap!')
a, b = b, a
print(f'a={a}, b={b}')
print('---')

print('2. add C: ')
c = a
print(f'c = a: {c}')
a = b
print(f'a = b: {a}')
b = c
print(f'b = c: {b}')
print(f'a={a}, b={b}')
