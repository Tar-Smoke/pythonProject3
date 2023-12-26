from datetime import *

def wd(year, month, day, period, work_d, rest_d):

    pt = period
    st = datetime(year, month, day)
    work_d = work_d
    rest_d = rest_d
    swd = []

    for x in range(pt):
        y = x
        td = timedelta(x)

        if y % (work_d + rest_d) >= work_d and y % (work_d + rest_d) != 0:
            pass
        else:
            swd.append(st + td)

    return swd
