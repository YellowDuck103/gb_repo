num = int(input("Введите любое целое число: "))
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
        if max_num == 9:
            break
    num //= 10
print(f"наибольшая цифра числа: {max_num}")