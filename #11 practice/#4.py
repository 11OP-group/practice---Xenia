num = int(input("Введите натуральное число: "))

def find_trois(x):
    c = 0  # кол-во троек в числе
    while x > 0:
        if x%10==3:
            c+=1
            x//=10
        else:
            x//=10
    return c
print(f"Кол-во цифр 3 в нём: {find_trois(num)}")

def last_digit(x):
    while x>0:
        c = 0 #счётчик кол-ва последней цифры в числе
        last = num%10
        while x>0:
            if x%10==last:
                c +=1
                x//=10
            else:
                x//=10
    return c
print(f"Последняя цифра встречается {last_digit(num)} раз")

def chet_digits(x):
    c = 0 #кол-во чётных цифр, счётчик
    while x>0:
        if (x%10)%2==0:
            c+=1
            x//=10
        else:
            x//=10
    return c
print(f"Кол-во чётных цифр: {chet_digits(num)}")

def summa_digits(x):
    s = 0 #счётчик суммы цифр
    while x>0:
        if x%10 > 5:
            s+=(x%10)
            x//=10
        else:
            x//=10
    return s
print(f"Сумма цифр больше 5 равна {summa_digits(num)}")

def proizvedenie_digits(x):
    s = 1 #счётчик произведения цифр
    while x>0:
        if x%10 > 7:
            s*=(x%10)
            x//=10
        else:
            x//=10
    return s
print(f"Произведение цифр, больших семи равно {proizvedenie_digits(num)}")

def fiveANDzero(x):
    c = 0 #счётчик кол-ва 5 и 0
    while x>0:
        if x%10 == 5 or x%10 == 0:
            c+=1
            x//=10
        else:
            x//=10
    return c
print(f"Кол-во цифр 0 и 5: {fiveANDzero(num)}")