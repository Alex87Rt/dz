# 1
# def multiplication_table(a, b):
#     for i in range(b + 1):
#         line = []
#         for j in range(a + 1):
#             if i == 0:
#                 line.append(j)
#             elif j == 0:
#                 line.append(i)
#             else:
#                 line.append(i * j)
#         print('\t'.join([str(i) for i in line]))
#
# multiplication_table(5, 3)
#
# import os
# # 2.
# def print_directory_contents(sPath):
#     """
#         Функция принимает имя каталога и распечатывает его содержимое
#         в виде «путь и имя файла», а также любые другие
#         файлы во вложенных каталогах.
#
#         Эта функция подобна os.walk. Использовать функцию os.walk
#         нельзя. Данная задача показывает ваше умение работать с
#         вложенными структурами.
#         """
#     def get(sPath):
#         line = []
#         for direct in os.listdir(sPath):
#             file_name = os.path.join(os.path.abspath(sPath), direct)
#             if os.path.isfile(file_name):
#                 line.append((os.path.abspath(sPath), direct))
#             else:
#                 line.extend(get(file_name))
#         return line
#     return print(get(sPath))
#
#
# print_directory_contents('/dz/lesson1')


# 3.
# def random_number_generator(a, b):
#     vocabulary = {}
#     list = []
#     for _ in range(10):
#         num = int((b - a) * random.random() + a)
#         list.append(num)
#         vocabulary.update({'elem_{}'.format(num): num})
#     return (list, vocabulary)
#
# print(random_number_generator(2, 5))
#
#
# 4.
def percent(number, months):
    if months not in [6, 12, 24]:
        return True

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= number < rate['end_sum']:
            return rate[months]
    return True


# def deposit(number, months):
#     perc = percent(number, months)
#     total = number
#     for month in range(months):
#         profit = total * perc / 100 / 12
#         total += profit
#     print(round(total))
#
# deposit(100000, 6)
# #
# # 5.
def charge_deposit(number, months, charge=1):
    perc = percent(number, months)
    total = number
    for month in range(months):
        profit = total * perc / 100 / 12
        total += profit
        if months != 0 and months != months - 1:
            total += charge + charge * perc / 100 / 12

    print(round(total))

charge_deposit(100000, 6, 200)