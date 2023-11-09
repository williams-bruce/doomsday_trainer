import sys
from datetime import date

def is_even(n:int)->bool:
    return n % 2 == 0


def is_leap_year(year:int)->bool:
    if year % 4 == 0 and not year % 100 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def digest_date(date:str)->tuple:
    '''Toma a data dada e quebra em dia, mes e ano. O formato da data é dd/mm/yyyy.'''
    day:str = date[:2]
    month:str = date[3:5]
    year:str = date[6:]
    try:
        _day = int(day)
        _month = int(month)
        _year = int(year)
    except ValueError:
        print("O formato da data está incorreto.")
        # return '0','0','0'
        sys.exit()

    return day, month, year


def pick_day()->int|str:
    '''Retorna um dia da escolha do usuário para o dia printado na tela'''
    print("""Escolha um numero para o dia:
          \t1. Domingo
          \t2. Segunda-feira
          \t3. Terça-feira
          \t4. Quarta-feira
          \t5. Quinta-feira
          \t6. Sexta-feira
          \t7. Sábado""")
    
    choice = ''
    while True:
        choice = input("Digite um número: ")
        if choice == 'exit':
            return 'exit'
        try:
            if int(choice) in range(1,8):
                break
            raise Exception
        except:
            print("Dígito inválido. Tente novamente...")
            continue
    
    return int(choice)


if __name__ == '__main__':
    data = date(1234,12,1)
    ndata = data.strftime('%d/%m/%Y')
    print(data)
    print(ndata)

 