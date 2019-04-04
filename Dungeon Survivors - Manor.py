def sec_convert(sec_total):
    sec = int(sec_total % 60)
    sec_tmp = int(sec_total / 60)
    mins = int(sec_tmp % 60)
    hours = int(sec_tmp / 60)
    time = list()
    time.append(str(hours) + 'h.')
    time.append(str(mins) + 'm.')
    time.append(str(sec) + 's.')
    return time


scale = 2

step = 22

food_cap = 220000
wood_cap = 200000
iron_cap = 160000
crystal_cap = 25000
mithril_cap = 25000

food_now = 163400
wood_now = 8700
iron_now = 77000
crystal_now = 1700
mithril_now = 1100

wood_cost = 2
iron_cost = 3
crystal_cost = 4
mithril_cost = 9

food_income = wood_income = iron_income = crystal_income = mithril_income = 1

craftsmen = 190
c = 0
while craftsmen > 0:

    try:
        food_ttf = int(((food_cap - food_now) / (food_income * scale)) * step)
    except ZeroDivisionError:
        food_ttf = 0
    try:
        wood_ttf = int(((wood_cap - wood_now) / (wood_income * scale)) * step)
    except ZeroDivisionError:
        wood_ttf = 0
    try:
        iron_ttf = int(((iron_cap - iron_now) / (iron_income * scale)) * step)
    except ZeroDivisionError:
        iron_ttf = 0
    try:
        crystal_ttf = int(((crystal_cap - crystal_now) / (crystal_income * scale)) * step)
    except ZeroDivisionError:
        crystal_ttf = 0
    try:
        mithril_ttf = int(((mithril_cap - mithril_now) / (mithril_income * scale)) * step)
    except ZeroDivisionError:
        mithril_ttf = 0

    if food_ttf <= 0:
        food_income += 1*scale
        craftsmen -= 1

    elif craftsmen <= 2:
        food_income += 1*scale
        craftsmen -= 1

    elif food_ttf > 0 and wood_ttf >= iron_ttf and wood_ttf >= crystal_ttf and wood_ttf >= mithril_ttf and craftsmen >= wood_cost + 1:
        wood_income += 1*scale
        craftsmen -= 1
        food_income -= wood_cost

    elif food_ttf > 0 and iron_ttf >= wood_ttf and iron_ttf >= crystal_ttf and iron_ttf >= mithril_ttf and craftsmen >= iron_cost + 1:
        iron_income += 1*scale
        craftsmen -= 1
        food_income -= iron_cost

    elif food_ttf > 0 and crystal_ttf >= iron_ttf and crystal_ttf >= wood_ttf and crystal_ttf >= mithril_ttf and craftsmen >= crystal_cost + 1:
        crystal_income += 1*scale
        craftsmen -= 1
        food_income -= crystal_cost

    elif food_ttf > 0 and mithril_ttf >= iron_ttf and mithril_ttf >= crystal_ttf and mithril_ttf >= wood_ttf and craftsmen >= mithril_cost + 1:
        mithril_income += 1*scale
        craftsmen -= 1
        food_income -= mithril_cost

    else:
        food_income += 1 * scale
        craftsmen -= 1

    if scale != 1 and craftsmen < 3 and c == 0:
        c += 1
        food_income -= 1
        wood_income -= 1
        iron_income -= 1
        crystal_income -= 1
        mithril_income -= 1

print('FOOD', food_income, '\nfill up after:', sec_convert(food_ttf))
print('WOOD', wood_income, '\nfill up after:', sec_convert(wood_ttf))
print('IRON', iron_income, '\nfill up after:', sec_convert(iron_ttf))
print('CRYSTAL', crystal_income, '\nfill up after:', sec_convert(crystal_ttf))
print('MITHRIL', mithril_income, '\nfill up after:', sec_convert(mithril_ttf))

