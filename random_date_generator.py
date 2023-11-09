import random
from datetime import date
from utils import is_leap_year

MONTHS_31 = (1,3,5,7,8,10,12)
MONTHS_30 = (4,6,9,11)

def generate_date()->str:
    '''generate a date between year 0 and year 2999'''
    year: int = random.randint(0,2999)
    month = random.randint(1,12)
    day: int = 0
    
    if month in MONTHS_30:
        day = random.randint(1,30)
    elif month in MONTHS_31:
        day = random.randint(1,31)
    elif month == 2:
        if is_leap_year(year):
            day: int = random.randint(1,29)
        else:
            day: int = random.randint(1,28)
    
    data = date(int(year), int(month), int(day))
    data = data.strftime('%d/%m/%Y')
    
    return data
        
if __name__ == '__main__':
    print(generate_date())
    print(generate_date())
    print(generate_date())