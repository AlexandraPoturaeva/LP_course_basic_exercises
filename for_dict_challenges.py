def make_freq_dict(students_list):
    names_list = list([x['first_name'] for x in students_list])
    freq_dict = {name: names_list.count(name) for name in set(names_list)}
    return freq_dict


def find_items_with_max_values(freq_dict):
    max_freq = max(freq_dict.values())
    max_freq_names = [name for name, freq in freq_dict.items() if freq == max_freq]
    return ', '.join(max_freq_names), max_freq


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('Задание 1')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_freq_dict = make_freq_dict(students)
for name, freq in name_freq_dict.items():
    print(f'{name}: {freq}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print('\nЗадание 2')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Оля'}
]

names_freq_dict = make_freq_dict(students)
result = find_items_with_max_values(names_freq_dict)
print(f'Чаще всего встречаются имена: {result[0]} ({result[1]} раз(a))')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('\nЗадание 3')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

print('Самые частые имена по классам / число повторений:')
for num, group in enumerate(school_students, start=1):
    group_names_freq_dict = make_freq_dict(group)
    result = find_items_with_max_values(group_names_freq_dict)
    print(f'\t№{num}: {result[0]} / {result[1]}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print('\nЗадание 4')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for group in school:
    group_name = group['class']
    gender_composition = {
        'f': 0,
        'm': 0
    }

    for student in group['students']:
        key = ('f', 'm')[is_male[student['first_name']]]
        gender_composition[key] += 1

    print(f'Класс {group_name}: девочки {gender_composition["f"]}, мальчики {gender_composition["m"]}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print('\nЗадание 5')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def count_group_gender_composition(group, gender_name_dict):
    gender_composition = [0, 0]
    for student in group['students']:
        gender_composition[gender_name_dict[student['first_name']]] += 1
    return gender_composition


school_gender_by_class = dict()
girls_by_class = dict()
boys_by_class = dict()

for group in school:
    class_name = group['class']
    girls_by_class[class_name], boys_by_class[class_name] = count_group_gender_composition(group, is_male)

school_gender_by_class['девочек'] = girls_by_class
school_gender_by_class['мальчиков'] = boys_by_class


for gender, breakdown in school_gender_by_class.items():
    result = find_items_with_max_values(breakdown)
    print(f'Больше всего {gender} в классах: {result[0]}')
