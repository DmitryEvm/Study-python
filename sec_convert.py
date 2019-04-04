def sec_convert(sec_total):
    sec = int(sec_total % 60)
    sec_tmp = int(sec_total / 60)
    mins = int(sec_tmp % 60)
    hours = int(sec_tmp / 60)
    time = list()
    time.append(str(hours))
    time.append(str(mins))
    time.append(str(sec))
#    if hours != 0:
#        time.append(str(hours))
#    if mins != 0 or (hours != 0 and mins == 0 and sec != 0):
#        time.append(str(mins))
#    if sec != 0:
#        time.append(str(sec))
#    if sec + mins + hours == 0:
#        time.append('no time data')
    return time
