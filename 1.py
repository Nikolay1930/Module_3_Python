"""name = input('Введите имя сотрудника: ')
salary = int(input('Введите зп сотрудника в месяц: '))
print('У', name, 'зп в год составляет', salary * 12, 'руб.')
print(f'У {name} зп в год составляет {salary * 12} руб.')"""

"""employee = {'name': 'Ваня', 'salary': 100_000}
print(f'У {employee["name"]} зп в год составляет {employee["salary"] * 12} руб.')
print(f'У {employee.get("name")} зп в год составляет {employee.get("salary") * 12} руб.')
print(employee)
employee['age'] = 22
print(employee)"""

"""employees_list = [
    {
        'name': 'Петя',
        'salary': 100_000
    },
    {
        'name': 'Ваня',
        'salary': 10_000
    },
    {
        'name': 'Игорь',
        'salary': 50_000
    }
]

for employee in employees_list:
    if employee['name'] == 'Ваня':
        employees_list.remove(employee)
        break

employees_list.append({'name': 'Олег', 'salary': 30_000})

# print(employees_list[-1])
for employee in employees_list:
    print(f'У {employee.get("name")} зп в год составляет {employee.get("salary") * 12} руб.')

print(len(employees_list))"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.on_work = True

    def get_info(self):
        print(f'У {self.name} зп в год составляет {self.salary * 12} руб.')


def get_info_employees(employees_list):
    for employee in employees_list:
        employee.get_info()


employees_list = [
    Employee('Петя', 100_000),
    Employee('Ваня', 10_000),
    Employee('Игорь', 50_000)
]

while True:
    print('-' * 80)
    print('1 - получить информацию о всех сотрудниках')
    print('2 - получить информацию об одном сотруднике')
    print('3 - выход')
    k = input('Введите номер команды: ')
    if k == '1':
        get_info_employees(employees_list)
    elif k == '2':
        name = input('Введите имя сотрудника: ')
        for employee in employees_list:
            if employee.name == name:
                employee.get_info()
                break
    else:
        print('Пока!')
        break


