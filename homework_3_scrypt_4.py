def navalny(n1, n2):
    return n1 ** n2
a = float(input("Введите число: "))
b = int(input("Введите отрицательное число: "))
while b >= 0:
    b = int(input("Введите отрицательное число: "))
print(navalny(a, b))
