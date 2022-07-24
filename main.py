field = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
         '6': ' ', '7': ' ', '8': ' ', '9': ' '}

figu = 'x'
player = 'первый'



def draw_field():
    print('=' * 40)
    print(" Нумерация клеток        Игровое поле")
    print(f'  -------------         -------------   ')
    print(f"  | 7 | 8 | 9 |         | {field['7']} | {field['8']} | {field['9']} |  ")
    print(f'  -------------         -------------   ')
    print(f"  | 4 | 5 | 6 |         | {field['4']} | {field['5']} | {field['6']} |  ")
    print(f'  ------------          -------------   ')
    print(f"  | 1 | 2 | 3 |         | {field['1']} | {field['2']} | {field['3']} |  ")
    print(f'  -------------         -------------')
    print('=' * 40)
    print('\n' * 2)


def clean_screen():
    print("\n" * 100)
    draw_field()


def print_fault():
    print('Некорректый ход! Поставьте свою фигуру в пустую клетку.\n')


def check_win():
    if field['1'] == field['2'] == field['3'] == figu or field['4'] == field['5'] == field['6'] == figu or field['7'] == \
            field['8'] == field['9'] == figu or field['1'] == field['4'] == field['7'] == figu or field['2'] == field[
        '5'] == field['8'] == figu or field['3'] == field['6'] == field['9'] == figu or field['1'] == field['5'] == \
            field['9'] == figu or field['7'] == field['5'] == field['3'] == figu:
        clean_screen()
        print(f'Выиграл {player} игрок.\n Игра окончена')
        return True
    return False


print('       Игра "крестики-нолики"')
print('')
print('Есть поле 3 х 3.  Первый игрок ставит в')
print('ячейку поля крестик, второй - нолик.')
print('Выигрывает тот, кто первым составит ряд ')
print('из трех своих фигур - по горизонтали,')
print('вертикали или по диагонали.')
print('Чтобы поставить фигуру в соответсвующюю')
print('ячейку, введите ее номер')

draw_field()



while True:
    print(f'Ходит {player} игрок\n')
    act = input()
    if act not in field or field[act] != ' ':
        clean_screen()
        print_fault()
        continue

    field[act] = figu
    clean_screen()

    if check_win():
        break

    if ' ' not in field.values():
        clean_screen()
        print('Ничья.\n Игра окончена')
        break

    if figu == 'x':
        figu = 'o'
        player = 'второй'
    else:
        figu = 'x'
        player = 'первый'


