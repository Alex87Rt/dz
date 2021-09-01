# # 1.
#
# def name_file(full_name):
#     return full_name.split('/')[1].split('.')[0]
#
# print(name_file('dz/main.py'))
#
#
# # 2
#
# def number(num):
#     number = float(num)
#     if int(number) == number:
#         return f'{num} - число целое'
#     else:
#         result = [f'{num} - дробное число, ']
#         L, R = num.split('.')
#         if L == R:
#             result.append('Левая и правая части совпадают - True')
#         else:
#             result.append('Левая и правая части не совпадают - False')
#         return ''.join(result)
#
#
# print(number(input('Введите число: ')))
#
# # 3
#
# def create_list(keys, values):
#     values.extend([None] * (len(keys) - len(values)))
#     return {key: value for (key, value) in zip(keys, values)}
#
# print(create_list([1, 2, 3, 4], ['Телефон', 'Компьютер', 'Планшет', 'Телевизор']))
# print(create_list([1, 2, 3, 4], ['Телефон', 'Компьютер', 'Планшет']))
# print(create_list([1, 2, 3, 4], ['Телефон', 'Компьютер', 'Планшет', 'Телевизор', 'Роутер']))
#
#
#
# # 4.
#
# import os
# import random
# import string
#
# len = 5
#
# def get_random_char():
#     return random.choice(string.ascii_letters)
#
# def get_random_string(length):
#     list = [get_random_char() for i in range(length)]
#     return ''.join(list)
#
# def create_file(name):
#     if os.path.isfile(name):
#         print('Файл с таким именем существует!!!!')
#         return False
#     with open(name, 'w', encoding='utf-8') as file:
#         num = [random.randint(0, 50) for _ in range(len)]
#         str = [get_random_string(len) for _ in range(len)]
#         file.writelines([f'({number} - {text})' for number, text in zip(num, str)])
#         return file
#
# def print_text_file(desc):
#     with open(desc.name, 'r', encoding='utf-8') as read_file:
#         for line in read_file:
#             print(line)
#
# file = create_file('lesson3_4.txt')
# if file:
#     print_text_file(file)
#
# # 5

import re

with open('lesson3_4.txt', encoding='utf-8') as source_file:
    with open('lesson3_5.txt', 'w', encoding='utf-8') as result_file:
        for line in source_file:
            text = re.findall(r'[a-z,0-9]+', 'example345')[0]
            result_file.writelines(re.sub(r'\d+', text, line))
