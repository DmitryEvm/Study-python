def sec_convert(sec_total):
    sec = int(sec_total % 60)
    sec_tmp = int(sec_total / 60)
    mins = int(sec_tmp % 60)
    hours = int(sec_tmp / 60)
    time = list()
    time.append(str(hours))
    time.append(str(mins))
    time.append(str(sec))
    return time
