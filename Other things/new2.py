num = [1,2,3,4,5]

def times_ten(x):
    return x * 10

num = list(map(times_ten, num))

print(num)


def check(x):
    return x > 25


num = list(filter(check, num))
print(num)


def add(x, y):
    return x + y


def do_twice(add, x, y):
    return add(add(x, y), add(x, y))


a = 5
b = 10

print(do_twice(add, a, b))


def countdown(s):
    while s > 0:
        yield s
        s -= 1


for i in countdown(3):
    print(f'{i}')


def decorator(say_hello):
    def wrap():
        print('----------')
        say_hello()
        print('----------')
    return wrap


@decorator
def say_hello():
    print('Hello world!')


say_hello()