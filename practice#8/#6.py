import random

print('Программа загадала случайное число. Попробуй его угадать:)')

n = random.randint(1,10)
count=3
a=0
while n!=a and count>0:
    a = int(input('Введите предполагаемое число '))
    if a==n:
          print('Угадали!')
          break

    else:
        count-=1
        if count > 0:
            print(f'Нет! Осталось {count} попытки')

if count == 0 and a != n:
    print(f'Попытки закончились! Было загадано число {n}')

