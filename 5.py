# with open('1.txt') as f:
#     print(f.readline())

'''import time


class RunningCodeJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'Время выполнения программы: {t} сек.')
        # print(f'{exc_type}\n{exc_val}\n{exc_tb}')
        print(exc_type, exc_val, exc_tb, sep='\n')
        # if exc_type is TypeError:
        #     return True
        return True


with RunningCodeJudge() as t1:
    lst = [i for i in range(1_000_000)]
    print(t1)
    1 / 0'''


'''lst = [1, 2, 3]
my_iterator = iter(lst)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

for i in my_iterator:
    print(i)
'''
from random import randint


class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit = self.__reload
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return randint(1, 100)


rand_iter = RandomIter(5)
# print(next(rand_iter))
for i in rand_iter:
    print(i)

for i in rand_iter:
    print(i)













