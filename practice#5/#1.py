salary = int(input("Введите свой годовой доход: "))
tax = (salary * 13 // 100)
tax_all = (salary - tax)

print (f"Общая сумма дохода: {salary: .2f} ")
print (f"Сумма рассчитанного налога: {tax: .2f} ")
print (f"Сумма «на руки» после вычета налога: {tax_all: .2f} ")
