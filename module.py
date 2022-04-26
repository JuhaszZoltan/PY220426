import os
import time

class Tesztkerdes:
    def __init__(self, feladvany:str, a:str, b:str, c:str, megoldas:str):
        self.feladvany = feladvany
        self.a = a
        self.b = b
        self.c = c
        self.megoldas = megoldas


def get_teszt() -> list[Tesztkerdes]:
    tesztsor:list[Tesztkerdes] = []
    kerdesek_file = open('teszt.txt', encoding='utf-8-sig')
    megoldasok_file = open('megoldas.txt', encoding='utf-8-sig')
    for x in range(15):
        k:str = kerdesek_file.readline().strip()
        a:str = kerdesek_file.readline().strip()
        b:str = kerdesek_file.readline().strip()
        c:str = kerdesek_file.readline().strip()
        m:str = megoldasok_file.readline().strip()
        tesztsor.append(Tesztkerdes(k, a, b, c, m))
    return tesztsor


def game_loop(tesztsor:list[Tesztkerdes]) -> int:
    pontszam:int = 0
    for f in tesztsor:
        print(f.feladvany)
        print(f'\t{f.a}')
        print(f'\t{f.b}')
        print(f'\t{f.c}')
        valasz:str = input('\nHelyes válasz betűjele: ')
        if valasz.lower() == f.megoldas.lower():
            print('HELYES!')
            pontszam += 1
        else:
            print(f'sajnos nem, a helyes válasz {f.megoldas}')
        time.sleep(3)
        os.system('cls')
    return pontszam