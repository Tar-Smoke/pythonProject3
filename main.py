from work_days import wd
# The schedule of working days
# Отримаємо вхідні дані
year = int(input("Start Year: "))
month = int(input("Start Month: "))
day = int(input("Start Day: "))
period = int(input("Period: "))
w_day = int(input("Work_days: "))
r_day = int(input("Rest days: "))
def schedule(year, month, day, period, w_day, r_day):
    print(wd(year, month, day, period, w_day, r_day))

if __name__ == '__main__':
    schedule(year, month, day, period, w_day, r_day)
