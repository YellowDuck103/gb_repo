def data_base(name, surname, year, city, mail, phone):
    my_str = name, surname, year, city, mail, phone
    return my_str
    
name = input("Enter your name: ")
surname = input("Enter your surname: ")
year = input("Enter your born year: ")
city = input("Enter your city: ")
mail = input("Enter your e-mail: ")
phone = input("Enter your phone number: ")

print(data_base(name, surname, year, city, mail, phone))
