def high_lit(var_1):
    if len(var_1) == 1:
        return var_1.capitalize()
    else:
            return var_1.title()
my_str = input("введите строку: ")
print(high_lit(my_str))
 