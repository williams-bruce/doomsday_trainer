import doomsday
import sys
import os
from random_date_generator import generate_date
from utils import pick_day
from time import time, sleep
from beautifultable import BeautifulTable
from termcolor import colored
from statistics import mean


class DoomsdayApp:
    def __init__(self):
        self.contador: int = 0
        self.acertos: list[bool]  = []
        self.datas: list[str] = []
        self.tempos: list[float] = []
        self.escolhas: list[tuple[str,str]] = []
    
    
    def run(self):
        os.system('cls')
        print('Bem vindo ao doomsday trainer!\n'+
              'Para cada data fornecida, digite o digito do dia da semana a que se referencia a data.\n'+
              'O treinador continua indefinidamente até que o usuário digite <exit>.')
        while True:
            escolha = input('Pronto para começar? (S/n): ')
            match(escolha):
                case 'N':
                    print('Até a próxima!')
                    print('Trainer interrompido pelo usuário')
                    sys.exit(0)
                case 'n':
                    print('Até a próxima!')
                    print('Trainer interrompido pelo usuário')
                    sys.exit(0)
                case 's':
                    os.system('cls')
                    self.contador += 1
                    break
                case 'S':
                    os.system('cls')
                    self.contador += 1
                    break
                case '':
                    os.system('cls')
                    self.contador += 1
                    break
                case _:
                    print('Dígito inválido. Tente novamente.')
                    continue
        
        try:
            while True:
                data = generate_date()
                self.datas.append(data)
                day_week = doomsday.doomsday(data)
                print(f'Data {self.contador}: {data}\n')
                start = time()
                escolha_usuario = pick_day()
                end = time()
                tempo_decorrido = end - start
                if escolha_usuario == 'exit':
                    self.contador -= 1
                    break
                elif day_week == doomsday.DAYS_NAMES[escolha_usuario % 7]:
                    print(f'Vc escolheu {doomsday.DAYS_NAMES[int(escolha_usuario) % 7]}')
                    print('Muito bom! Resposta correta!')
                    print(f'Tempo de decisão: {tempo_decorrido:.2f} s')
                    self.acertos.append(True)
                else:
                    print(f'Vc escolheu {doomsday.DAYS_NAMES[int(escolha_usuario) % 7]}')
                    print(f"Errado!")
                    print(f'Correto: {day_week}')
                    print(f'Tempo de decisão: {tempo_decorrido:.2f} s')
                    self.acertos.append(False)
                
                self.escolhas.append((day_week, doomsday.DAYS_NAMES[int(escolha_usuario) % 7]))
                self.tempos.append(tempo_decorrido)
                self.contador += 1
                sleep(5)
                os.system('cls')
        
        except KeyboardInterrupt:
            self.contador -= 1
            print('\n\nTrainer interrompido pelo usuário\n\n')


    def show_report(self):
        table = BeautifulTable()
        table.columns.header = ['Data', 'Dia correto', 'Dia escolhido', 'Tempo de decisão']
        for i in range(len(self.acertos)):
            if self.acertos[i]:
                table.rows.append([self.datas[i], self.escolhas[i][0], colored(self.escolhas[i][1],'green'), self.tempos[i]])
            else:
                table.rows.append([self.datas[i], self.escolhas[i][0], colored(self.escolhas[i][1],'red'), self.tempos[i]])
        table.rows.header = [str(i+1) for i in range(len(self.acertos))]
        os.system('cls')
        print('\n*****************     SEU RELATÓRIO DE TREINO     *****************\n')
        print(table)
        print(f'Vc treinou com {self.contador} datas.')
        print(f'Vc acertou {self.acertos.count(True)} datas.')
        print(f'Vc errou {self.acertos.count(False)} datas.')
        print(f'Sua média de tempo: {mean(self.tempos):.2f} s.')
        


if __name__ == '__main__':
    app = DoomsdayApp()
    app.run()
    app.show_report()

