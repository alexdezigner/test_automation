# Andreychikov Alexandr // Md-PT2-17-21-3 // Automatic testing in Python

# Homework 7

# Ex.1. Calculator

wrong = "Вы должны ввести число!"
while True:
    symbol = input("Выбирете действие  '+', '-', '*', '/' : ")
    if symbol in ('+', '-', '*', '/'):
        a = input("Num1 is: ")
        try:
            a == float(a)
            b = input("Num2 is: ")
            try:
                b == float(b)
                print(eval(a + symbol + b))
            except ZeroDivisionError:
                print("На 0 делить нельзя!")
            except ValueError:
                print(wrong)
        except ValueError:
            print(wrong)
    else:
        if symbol == "end":
            print("Пока!")
            break
        else:
            print("Выбирайте действие!")
            print("(если хотите закончить введите 'end')")

# Ex.2. Coder-Decoder 'Cesar'
import string
choice = '12Ee'
action = ' '

def caesar_encrypt(your_text, step):
    out_text = ""
    upper_eng = string.ascii_uppercase
    lower_eng = string.ascii_lowercase
    upper_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    lower_rus = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    for src_letter in your_text:
        if src_letter in upper_eng:
            index = upper_eng.index(src_letter)
            if action == '1':
                crypt = (index + step) % 26
            else:
                crypt = (index - step) % 26
            new_letter = upper_eng[crypt]
            out_text = out_text + new_letter
        elif src_letter in upper_rus:
            index = upper_rus.index(src_letter)
            if action == '1':
                crypt = (index + step) % 33
            else:
                crypt = (index - step) % 33
            new_letter = upper_rus[crypt]
            out_text = out_text + new_letter
        elif src_letter in lower_eng:
            index = lower_eng.index(src_letter)
            if action == '1':
                crypt = (index + step) % 26
            else:
                crypt = (index - step) % 26
            new_letter = lower_eng[crypt]
            out_text = out_text + new_letter
        elif src_letter in lower_rus:
            index = lower_rus.index(src_letter)
            if action == '1':
                crypt = (index + step) % 33
            else:
                crypt = (index - step) % 33
            new_letter = lower_rus[crypt]
            out_text = out_text + new_letter
        else:
            out_text = out_text + src_letter
    return out_text

print("1 - encoding \n2 - decoding \nE - exit")
while action not in choice:
    action = input('>>>')
if action == "E" or action == "e":
    print("Well done! Bye!")
    exit(0)
else:
    mess = input('Enter your message: ')
    while True:
        step = input('Enter key: ')
        if step == '0':
            print('Key cannot be "0" !')
        else:
            if step.isdecimal():
                step = int(step)
                break
            else:
                print('Enter an integer!')

    print('Message: ' + mess)
    print('Processed: ' + caesar_encrypt(mess, step))
    print()



# Ex.2*. My Coder-Decoder
'''
Принцип работы:
за основу взят шифр Атбаш (когда первая буква в алфавите заменяется последней, вторая- предпоследней и т.д.). 
И доработка - при каждом обращении к следующему символу, весь алфавит сдвигается. *почти Enigma)))
'''

import string

def my_encrypt(your_text):
    out_text = ""
    upper_eng = string.ascii_uppercase
    lower_eng = string.ascii_lowercase
    upper_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    lower_rus = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    nomers = string.digits
    for src_letter in your_text:
        if src_letter in upper_eng:
            index = 1 + upper_eng.index(src_letter)
            new_letter = upper_eng[-index]
            out_text = out_text + new_letter
            upper_eng = upper_eng[1:] + upper_eng[0]
        elif src_letter in upper_rus:
            index = 1 + upper_rus.index(src_letter)
            new_letter = upper_rus[-index]
            out_text = out_text + new_letter
            upper_rus = upper_rus[1:] + upper_rus[0]
        elif src_letter in lower_eng:
            index = 1 + lower_eng.index(src_letter)
            new_letter = lower_eng[-index]
            out_text = out_text + new_letter
            lower_eng = lower_eng[1:] + lower_eng[0]
        elif src_letter in lower_rus:
            index = 1 + lower_rus.index(src_letter)
            new_letter = lower_rus[-index]
            out_text = out_text + new_letter
            lower_rus = lower_rus[1:] + lower_rus[0]
        elif src_letter in nomers:
            index = 1 + nomers.index(src_letter)
            new_letter = nomers[-index]
            out_text = out_text + new_letter
            nomers = nomers[1:] + nomers[0]
        else:
            out_text = out_text + src_letter
    return out_text
mess = input('Enter your message: ')
print('Message: ' + mess)
print('Processed: ' + my_encrypt(mess))
print()
