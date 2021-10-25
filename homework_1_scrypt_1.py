name = input("введите ваше имя: ")
age = int(input("сколько вам лет?"))
if age < 18:
    gender = input("вы мальчик или девочка ")
else:
    gender = input("Вы мужчина или женщина? ")
print("Здравствуйте, ", name, "вы ", gender, "и вам", age, "лет")

