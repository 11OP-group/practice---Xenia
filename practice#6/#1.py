temp = int(input("Введите температуру: "))
davl = int(input("Введите давление: "))
puls = int(input("Введите пульс: "))

if temp==36 and 110<=davl<=130 and 60<=puls<=100:
    print('Нормальное состояние')
elif (temp==35 or temp==37 or temp==38) and (105<=davl<=110 or 130<=davl<=140)\
        and (55<=puls<=60 or 100<=puls<=110):
    print('Легкое недомогание')
elif (temp< 35 or temp>=38) or (davl <105 or davl >140)\
    or (puls <55 or puls >110):
    print('Требуется врач')
