student = {} # создали словарь
student ['name'] = str(input("Ваше имя: "))
student["age"] = int(input("Ваш возраст: "))
student['sub'] = str(input("Любимые предметы (через запятую): "))

print('=' * 30)
print('АНКЕТА СТУДЕНТА')
print('=' * 30)
print(f'Имя: {student['name']}')# через префикс обращаемся кс ловарю и берем нужную переменную
print(f'Возраст: {student['age']}')
print(f'Любимые предметы: {student['sub']}')
print('=' * 30)
