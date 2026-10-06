weight, height = map(float, input("Введите Ваш вес и рост: ").split())
imt = weight / (height ** 2)

print(f"ИМТ: {imt:.1f}")
