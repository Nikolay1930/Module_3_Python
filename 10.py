import os
'''path = r'C:\python\work_to_ege\DS\3MOD\27\12_01_06.py'
current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..')

print(current_path)'''


'''def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n


print(f(10))'''

'''
f(6) = f(5) + 6 = 15 + 6 = 21
f(5) = f(4) + 5 = 10 + 5 = 15
f(4) = f(3) + 4 = 6 + 4 = 10
f(3) = f(2) + 3 = 3 + 3 = 6
f(2) = f(1) + 2 = 1 + 2 = 3
f(1) = 1

'''
'''import sys
sys.setrecursionlimit(3000)


def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 4 * f(n - 1)


print(f(2300) / f(2290))'''


def get_all_files(path, st):
    for my_file in os.listdir(path):
        new_path = os.path.join(path, my_file)
        if os.path.isdir(new_path):
            print(f'{st}Папка: {my_file}')
            get_all_files(new_path, st + '    ')
        else:
            print(f'{st}-{my_file}')


get_all_files('C:\python\work_to_ege\DS', '')



















