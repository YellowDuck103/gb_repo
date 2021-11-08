name = input("Введите название товара: ")
cost = int(input("Введите стоимость: " ))
volume = int(input("Введите количество штук: "))
my_dict_1 = {"Название": name,
"Цена": cost,
"Количество": volume}
ek_1 = (1, my_dict_1)

name_2 = input("Введите название товара: ")
cost_2 = int(input("Введите стоимость: " ))
volume_2 = int(input("Введите количество штук: "))
my_dict_2 = {"Название": name_2,
"Цена": cost_2,
"Количество": volume_2}
ek_2 = (2, my_dict_2)

name_3 = input("Введите название товара: ")
cost_3 = int(input("Введите стоимость: " ))
volume_3 = int(input("Введите количество штук: "))
my_dict_3 = {"Название": name_3,
"Цена": cost_3,
"Количество": volume_3}
ek_3 = (3, my_dict_3)

anal = {"Название": [name, name_2, name_3], "Цена": [cost, cost_2, cost_3], "Количество": [volume, volume_2, volume_3]}
print(anal)
