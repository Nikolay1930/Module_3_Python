# import time
#
# t1 = time.time()
# lst = (time.sleep(i) for i in range(1, 4))
# t2 = time.time()
#
# print(lst, t2-t1)
# t1 = time.time()
# for elem in lst:
#     print(elem)
# t2 = time.time()
# print(t2 - t1)

# r = range(1, 100)
# print(list(r))
# for i in r:
#     print(i)


# def not_lazy_func():
#     for i in range(5):
#         return i
#
#
# def lazy_func():
#     for i in range(5):
#         print('до i')
#         yield i
#         print('после i')
#
#
# print(lazy_func())
#
# for elem in lazy_func():
#     print(elem)


# lst = [1, 2, 4]
#
#
# def lazy_func(my_lst):
#     # for elem in my_lst:
#     #     yield elem
#     yield from my_lst
#
#
# for i in lazy_func(lst):
#     print(i)

# f = open('1.txt', 'w')
# f.write('hi')
# f.close()

# with open('1.txt', 'w') as f:
#     f.write('hiiiiiiiiiiiiiiiiii')
#     print(f.closed)
# print(f.closed)


'''import contextlib


@contextlib.contextmanager
def str_reverse(my_str):
    print('Вошли в менеджер контекста.')
    yield my_str[::-1]
    print('Выходим из контекстного менеджера...')


with str_reverse('Hello') as s:
    print(f'Выполняем действия: {s}')
'''

# import contextlib
#
#
# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print(f'Произошло исключение - {exc}')
#
#
# with exc_handler(IndexError):
#     lst = [2, 4, 5]
#     print(lst[9999999])
#     print(2)
#
# print(1)


def func(*args, **kwargs):
    print(f'Арги: {args}\nКварги: {kwargs}')


func(1, 3 ,3, 3,3,3,3,3,3,3,3,3,3, a=3, x=7, z=191919)