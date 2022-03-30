from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def school():
    for item in zip_longest(tutors, klasses):
        yield item


students = school()
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))
