

from enum import Enum


Menu = Enum('Menu', ['push', 'pop', 'peek', 'search', 'dump', 'close'])

#메뉴 선택
def select_menu():
    s = [f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s, sep='     ', end='    ')
            n = int(input(': '))
            if 1<= n <=len(Menu):
                return Menu
