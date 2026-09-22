my_list = [1, 2, 3]
my_list[0]=6 #меняем первое значение по индексу на желаемое
print(my_list)

my_tuple = (1, 2, 3)
my_tuple[0]= 5
print(my_tuple) # в кортежи после создания нельзя вносить изменения

my_string = "cat"
my_string[0] = 'b'
print(my_string) # объект типа стр не поддерживает присваивания по индексу
