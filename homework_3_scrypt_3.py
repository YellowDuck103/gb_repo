def summ_arg(n1, n2, n3):
    if n1 < n2 < n3:
        return n2 + n3
    elif n3 < n2 < n1:
            return n1 + n2
    elif n2 < n1 < n3:
            return n3 + n1
    elif n1 < n3 < n2:
            return n2 + n3
    elif n2 < n3 < n1:
            return n3 + n1
    elif n3 < n1 < n2:
            return n1 + n2
            
n1 = int(input("Введите число n1: "))
n2 = int(input("Введите число n2: "))
n3 = int(input("Введите число n3: "))
print(summ_arg(n1, n2, n3))
