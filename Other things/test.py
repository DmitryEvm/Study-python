def leap(y):
    if y % 4 == 0 and not (y % 100 == 0 and y % 400 != 0):
        return True
    else:
        return False


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

