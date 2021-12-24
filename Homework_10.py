# Andreychikov Alexandr // Md-PT2-17-21-3 // Automatic testing in Python

# Homework 10

# Ex.1.

import re
#  import docx


def desintegrator(form):
    while '(' in form:
        skobki = re.search(r'\(\w+\)', form).group()[1:-1]
        skoba_end = re.search(r'\(\w+\)', form).end()
        skoba_start = re.search(r'\(\w+\)', form).start()
        v_skobkah = ''
        for i in skobki:
            if i.isalpha():
                if i.isupper():
                    element = i
                    v_skobkah += i
                elif i.islower():
                    element += i
                    v_skobkah += i
            elif i.isdigit():
                v_skobkah += element * (int(i) - 1)
                element = ''
        if form[skoba_end].isdigit():
            v_skobkah *= int(form[skoba_end])
        form = (f'{form[:skoba_start]}{v_skobkah}{form[skoba_end + 1:]}')
        return desintegrator(form)
    return form


def atom(func):
    given_string = func
    result_string = ''
    for i in given_string:
        if i.isalpha():
            if i.isupper():
                element = i
                result_string += i
            elif i.islower():
                element += i
                result_string += i
        elif i.isdigit():
            result_string += element * (int(i) - 1)
    elements_list = re.findall(r'[A-Z][^A-Z]*', result_string)
    elements_dict = {i: elements_list.count(i) for i in elements_list}
    return elements_dict

# --- старт ---


#  mendeleev = docx.Document('Mendeleev_table.docx')
form = input('Введите формулу вещества : ')
form = form.replace('{' or '[', '(').replace('}' or ']', ')').replace(' ', '')
form = re.sub(r'\)(?!\d+)', ')1', form)
for key, value in atom(desintegrator(form)).items():
    ''' при наличии модудя -docx- можно реализовать проверку 
        вводимых элементов
    if key is not mendeleev.paragraphs:
        print('Введен неизвестный элемент!')
        exit(0)
        '''
    print(f'{key} : {value}')
