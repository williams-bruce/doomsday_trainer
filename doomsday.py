from utils import is_even, is_leap_year, digest_date

data_teste:str = '16/02/1996'

CENTURY_DAYS: tuple[int] = (3,1,6,4)
DAYS_YEAR: tuple[int] = (3,28,0,4,9,6,11,8,5,10,7,12)
DAYS_LEAP_YEAR: tuple[int] = (4,29,0,4,9,6,11,8,5,10,7,12)
DAYS_NAMES: tuple[str] = ('Saturday','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

def doomsday(date:str)->str:
    day, month, year = digest_date(date)

    year1:int = int(year[2:])
    if is_even(year1):
        year1 //= 2
    elif not is_even(year1):
        year1 += 11
        year1 //= 2
    
    if not is_even(year1):
        year1 += 11
    
    y: int = year1 % 7
    y = 7 - y
    
    year_day: int = (CENTURY_DAYS[int(year[:2]) % 4] + y) % 7
    
    month: int = int(month)
    week_day: int = 0
    if is_leap_year(int(year)):
        day_in_month: int = DAYS_LEAP_YEAR[month - 1]
        dif: int = int(day) - day_in_month
        week_day = (year_day + dif) % 7
    else:
        day_in_month: int = DAYS_YEAR[month - 1]
        dif: int = int(day) - day_in_month
        week_day = (year_day + dif) % 7
    
    return DAYS_NAMES[week_day]
    


if __name__ == '__main__':
    print(f'A data é {data_teste}. Este dia foi {doomsday(data_teste)}')