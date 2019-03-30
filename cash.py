item1 = 8
item2 = 43
item3 = 22
item4 = 12
cash_in = 0
cash = 0
to_pay = item1 + item2 + item3 + item4

print('Сумма к оплате:', to_pay)
while cash_in < to_pay:
    cash = int(input("Получено денег: "))
    cash_in = cash_in + cash
    if cash_in == to_pay:
        print('Денег достаточно, сдачи не нужно.')
    elif cash_in > to_pay:
        print('Денег достаточно, сдача: ', cash_in - to_pay)
    elif cash_in < to_pay:
        print("Недостаточно денег. Нужно еще: ", to_pay - cash_in)

print("Печать чека.")