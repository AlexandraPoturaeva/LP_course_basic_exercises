# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = set([x['first_name'] for x in students])

for name in names:
    name_count = 0
    for student in students:
        if name == student['first_name']:
            name_count += 1
    print(f'{name}: {name_count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Оля'}
]

names = set([x['first_name'] for x in students])
names_freq_dict = dict()

for name in names:
    name_count = 0
    for student in students:
        if name == student['first_name']:
            name_count += 1
    names_freq_dict[name] = name_count

max_freq = max(names_freq_dict.values())
max_freq_names_positions = [index for index, value in enumerate(list(names_freq_dict.values()))
                            if value == max_freq]
max_freq_names = [list(names_freq_dict.keys())[pos] for pos in max_freq_names_positions]
max_freq_names_str = ', '.join(max_freq_names)

print(f'Чаще всего встречаются имена: {max_freq_names_str} ({max_freq} раз(a))')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

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
for num, group in enumerate(school_students):
    # формирую частотный словарь имён в классе {имя: частота}
    students = [student['first_name'] for student in group]
    student_unique_names = set(students)
    student_names_freq_dict = {name: students.count(name) for name in student_unique_names}

    # считаю, какое имя чаще всего встречается
    max_freq = max(student_names_freq_dict.values())  # нахожу максимальное значение частоты

    # создаю список позиций (индексов) элементов с максимальной частотой в частотном словаре имён
    max_freq_names_positions = [
        index
        for index, value in enumerate(list(student_names_freq_dict.values()))
        if value == max_freq
    ]

    # формирую список самых частых имён
    max_freq_names = [list(student_names_freq_dict.keys())[pos] for pos in max_freq_names_positions]
    max_freq_names_str = ', '.join(max_freq_names)

    print(f'\t№{num + 1}: {max_freq_names_str} / {max_freq}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

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
        'ж': 0,
        'м': 0
    }
    for student in group['students']:
        if is_male[student['first_name']]:
            gender_composition['м'] += 1
        if not is_male[student['first_name']]:
            gender_composition['ж'] += 1

    print(f'Класс {group_name}: девочки {gender_composition["ж"]}, мальчики {gender_composition["м"]}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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

school_gender_by_class = dict()
girls_by_class = dict()
boys_by_class = dict()

for group in school:
    class_name = group['class']
    boys = 0
    girls = 0
    for student in group['students']:
        if is_male[student['first_name']]:
            boys += 1
        if not is_male[student['first_name']]:
            girls += 1
    girls_by_class[class_name] = girls
    boys_by_class[class_name] = boys

school_gender_by_class['девочек'] = girls_by_class
school_gender_by_class['мальчиков'] = boys_by_class

for gender, breakdown in school_gender_by_class.items():
    max_gender_cnt = max(breakdown.values())
    classes_with_max_gender_cnt = [key for key, value in breakdown.items() if value == max_gender_cnt]
    result = ', '.join(classes_with_max_gender_cnt)
    print(f'Больше всего {gender} в классах: {result}')
