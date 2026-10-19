import time
import sys
import os
import math

BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
YELLOW = '\u001b[43m'
CYAN = '\u001b[46m'
GREEN = '\u001b[42m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


def rectangle():
    positions = [(3, 5), (3, 15), (8, 15), (8, 5)]

    for row, col in positions:
        print('\u001b[2J\u001b[H', end='')
        print(f'\u001b[{row};{col}H{RED}    {RESET}', end='', flush=True)
        time.sleep(1)


def graph():
    print('\u001b[2J\u001b[H', end='')

    width = 50

    for y in range(5, -1, -1):
        line = ''

        for x in range(width + 1):
            value = math.sqrt(x / width * 25)

            if round(value) == y:
                line += YELLOW + '*' + RESET
            else:
                line += ' '

        print(f'{y} |{line}')

    print('  +' + '-' * (width + 1))
    print('   0         5         10        15        20        25')


def flag():
    pixel = '    '
    width = 10

    for i in range(4):
        print(WHITE + pixel * width + RESET)

    for i in range(4):
        print(RED + pixel * width + RESET)


def figure():
    bar = '▮' * 20
    stem = ' ' * 9 + '▮' + ' ' * 9
    sides = ' ' * 3 + '▮' + ' ' * 12 + '▮'

    figure = [bar, stem, stem, bar, sides, sides, bar]

    for line in figure:
        print(CYAN + line + RESET)

def sequence():
    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, 'sequence.txt')

    if not os.path.isfile(filename):
        filename = os.path.join(folder, 'sequence(1).txt')

    with open(filename, 'r', encoding='utf-8') as file:
        numbers = []

        for line in file:
            if line.strip():
                numbers.append(float(line))

    first = numbers[:125]
    second = numbers[125:250]

    avg1 = sum(abs(x) for x in first) / 125
    avg2 = sum(abs(x) for x in second) / 125

    total = avg1 + avg2

    print(f'\nСреднее первых 125 чисел: {avg1:.5f}')
    print(f'Среднее следующих 125 чисел: {avg2:.5f}')

    p1 = avg1 / total * 100
    p2 = avg2 / total * 100

    print(f'\nПервые 125 чисел | {BLUE}{" " * round(p1 / 2)}{RESET} {p1:.2f}%')
    print(f'Следующие 125 чисел | {GREEN}{" " * round(p2 / 2)}{RESET} {p2:.2f}%')



rectangle()
graph()
flag()
figure()
sequence()
