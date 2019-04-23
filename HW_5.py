def empty():
    pass


# х2
def x2(a):
    return a * 2


# odd or no? o.o
def is_odd(number):
    if number % 2 == 0:
        print("Yes")
    else:
        print("no")


is_odd(23)
print(x2(67))


# comparison
def comp(arg1, arg2=10):
    if arg1 > arg2:
        print("yes")
    else:
        print("no")


comp(123, 12)

# lambda
x = lambda a, b: a % b
print(x(123, 12))


# decorator
def decor(func):
    def wrapper():
        print("--=={ begin }==--")
        func()
        print("--=={  end  }==--")

    return wrapper


@decor
def function():
    print("Hello -.-")


function()


# map, filter
def plus(x):
    return x + 5


num = [12, 23, 34, 45, 56, 67, 78, 89]
print(list(map(plus, num)))


def plus(x):
    return x % 2 == 0


num = [12, 23, 34, 45, 56, 67, 78, 89]
print(list(filter(plus, num)))


# min, max
def minmax(*x):

    return [min(x), max(x)]


print(minmax(134, 24, 11, 78, 52))


# leap year
def leap(y):
    if y % 4 == 0 and not (y % 100 == 0 and y % 400 != 0):
        return True
    else:
        return False


print(f'2012 год високосный: ', leap(2012))
print(f'2100 год високосный: ', leap(2100))


# список високосных годов
def leap_list(beg, end):
    return [i for i in range(beg, end + 1) if i % 4 == 0 and not (i % 100 == 0 and i % 400 != 0)]


print(leap_list(2000, 2100))


# season
def season(month):
    if month == 12 or 0 < month < 3:
        return 'winter'
    elif month in range(3, 5+1):
        return 'spring'
    elif month in range(6, 8+1):
        return 'summer'
    elif month in range(9, 11+1):
        return 'autumn'
    else:
        return 'error'


some_month = 11
print('season:', season(some_month))


# внутри используется LEAP
def date(d, m, y):
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    m_30 = [4, 6, 9, 11]
    if d in range(1, 31+1) and m in range(1, 12+1) and y in range(1900, 2100 + 1):
        if d == 31 and m in m_31 or d < 31 and m in m_30:
            return True
        elif (leap(y) and d <= 29) or (not leap(y)) and d <= 28:
            return True
        else:
            return False
    else:
        return False


print('date(29, 2, 2012):', date(29, 2, 2012))
print('date(29, 2, 2013):', date(29, 2, 2013))
print('date(31, 5, 2019):', date(31, 5, 2019))
print('date(31, 6, 2019):', date(31, 6, 2019))


l = [16, -17, 2, 78.7, False, False, {'True', True}, 555, 12, 23, 42, 'DD']
new = list()


def list_transform(old):
    for item in old:
        if type(item) == int or type(item) == float:
            new.append(item)

    return sorted(new)


print(list_transform(l))
