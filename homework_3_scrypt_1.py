def deli(arg_1, arg_2):
    return arg_1 / arg_2
arg_1 = int(input("Введите делимое: "))
arg_2 = int(input("Введите делитель: "))
while arg_2 == 0:
    arg_2 = int(input("Введите число отличное от 0: ")
print(deli(arg_1, arg_2))
