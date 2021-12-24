# Andreychikov Alexandr // Md-PT2-17-21-3 // Automatic testing in Python

# Homework 5


# Ex.1. Игра "быки - коровы"

import random


def comp_number():
    compNum.insert(0, random.randint(0, 9))
    for i in range(1, 4):
        a = random.randint(0, 9)
        while a in compNum:
            a = random.randint(0, 9)
        compNum.insert(i, a)
    return compNum


def play(compNum, yourNum, cow, bull, bonus, end):
    # 1.Определяем кол-во "коров"
    for i in range(len(compNum)):
        if str(compNum[i]) in yourNum:
            cow += 1
    # 2.Определяем количество "быков"
    for i in range(len(compNum)):
        if str(compNum[i]) == yourNum[i]:
            bull += 1
            cow = cow - 1
    # 3.Проверяем количество "быков"==4 --> ВЫЙГРЫШ
    if bull == 4:
        end = 0
        yourNum = 'exit'
    # 4.Выдаем кол-во "коров" и "быков"
    if bull != 4:
        print('КОРОВ: ' + str(cow) + ' | ' + 'БЫКОВ: ' + str(bull))
        bonus = bonus - 1
    return compNum, yourNum, cow, bull, bonus, end


# Начальные установки и запуск
compNum = []
yourNum = ''
d = ''
end = ''
test = 0
bonus = 101
print('Добро пожаловать!')
print('Вам необходимо угадать четырехзначное число.')
print('Максимум можно заработать 100 баллов,')
print('если угадать число со второй попытки :-))')
print('(для ВЫХОДА из игры наберите "exit")')
print('(для запуска в тест.режиме введите "test")')
input('press ENTER to continue...')
# старт игры
if __name__ == '__main__':
    compNum = comp_number()
    while yourNum != 'exit':
        print("Введите ваше число:")
        yourNum = input()
        cow = 0
        bull = 0
        if len(yourNum) == 4:
            if yourNum == 'test':
                print('Компьютер загадал число:')
                test = 1
                print(*compNum)
            elif yourNum.isnumeric():
                for m in range(len(yourNum)):
                    for k in range(len(yourNum)):
                        if m != k:
                            if yourNum[m] == yourNum[k]:
                                if yourNum[m] not in d:
                                    d = d + yourNum[m]
                if d != '':
                    print('У вас повторяется "' + d + '"')
                    d = ''
                else:
                    compNum, yourNum, cow, bull, bonus, end = play(compNum, yourNum, cow, bull, bonus, end)
            else:
                print('Вы должны ввести только цифры!')
        else:
            print("вы должны ввести 4 цифры")
            print("цифры не должны повторяться")

    if end == 0:
        print('Поздравляем! Вы угадали!')
        if test == 1:
            print('Вам не начислены очки, т.к. игра запущена в ТЕСТ-режиме.')
        else:
            print('||||  Вы набрали : ' + str(bonus) + ' очк.  ||||')
    elif end == '':
        print('Вы вышли из игры! Очень жаль.')
    exit(0)
