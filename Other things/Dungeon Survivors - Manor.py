def sec_convert(sec_total):
    sec = int(sec_total % 60)
    sec_tmp = int(sec_total / 60)
    mins = int(sec_tmp % 60)
    hours = int(sec_tmp / 60)
    time = list()
    time.append(str(hours).zfill(2) + 'h.')
    time.append(str(mins).zfill(2) + 'm.')
    time.append(str(sec).zfill(2) + 's.')
    return time


cmen = 215 - 5
prod = 2
step = 20

food_cap = 300000
wood_cap = 320000
iron_cap = 230000
crystal_cap = 40000
mithril_cap = 35000
res_cap = [food_cap, wood_cap, iron_cap, crystal_cap, mithril_cap]

food_now = 19600
wood_now = 30500
iron_now = 210000
crystal_now = 16200
mithril_now = 32000
res_now = [food_now, wood_now, iron_now, crystal_now, mithril_now]

food_cmen = wood_cmen = iron_cmen = crystal_cmen = mithril_cmen = 1
res_cmen = [food_cmen, wood_cmen, iron_cmen, crystal_cmen, mithril_cmen]

res_cost = [0, 2, 3, 4, 9]

res_ttf = [0] * 5

for i in range(len(res_ttf)):
    total_cost = res_cmen[1] * res_cost[1] + res_cmen[2] * res_cost[2] + \
                 res_cmen[3] * res_cost[3] + res_cmen[4] * res_cost[4]
    if i == 0:
        res_ttf[i] = int(((res_cap[i] - res_now[i]) / (res_cmen[i] * prod - total_cost)) * step)
    else:
        res_ttf[i] = int(((res_cap[i] - res_now[i]) / (res_cmen[i] * prod)) * step)

x = 0
count1 = count2 = count3 = count4 = 0
while cmen > 0:
    x += 1
    for i in range(len(res_ttf)):
        total_cost = res_cmen[1] * res_cost[1] + res_cmen[2] * res_cost[2] + \
                     res_cmen[3] * res_cost[3] + res_cmen[4] * res_cost[4]

        if res_ttf[0] == max(res_ttf) and cmen > res_cost[i]:
            temp = res_ttf.copy()
            temp.remove(temp[0])
            x = res_ttf.index(max(temp))
            res_cmen[x] += 1
            count1 += 1
            cmen -= 1
            res_ttf[x] = int(((res_cap[x] - res_now[x]) / (res_cmen[x] * prod)) * step)

        if max(res_ttf) == res_ttf[i] and res_ttf[0] >= 0 and cmen > res_cost[i]:
            res_cmen[i] += 1
            cmen -= 1
            count2 += 1
            if i == 0:
                try:
                    res_ttf[i] = int(((res_cap[i] - res_now[i]) / ((res_cmen[i] * prod) - total_cost)) * step)
                except ZeroDivisionError:
                    res_ttf[i] = 0
            else:
                res_ttf[i] = int(((res_cap[i] - res_now[i]) / (res_cmen[i] * prod)) * step)

        else:
            if cmen > 0:
                res_cmen[0] += 1
                cmen -= 1
                count3 += 1
                try:
                    res_ttf[0] = int(((res_cap[0] - res_now[0]) / ((res_cmen[0] * prod) - total_cost)) * step)
                except ZeroDivisionError:
                    res_ttf[0] = 0
            else:
                break

print(f'FOOD:    {sec_convert(res_ttf[0])} Craftsmen: {res_cmen[0]}')
print(f'WOOD:    {sec_convert(res_ttf[1])} Craftsmen: {res_cmen[1]}')
print(f'IRON:    {sec_convert(res_ttf[2])} Craftsmen: {res_cmen[2]}')
print(f'CRYSTAL: {sec_convert(res_ttf[3])} Craftsmen: {res_cmen[3]}')
print(f'MITHRIL: {sec_convert(res_ttf[4])} Craftsmen: {res_cmen[4]}')