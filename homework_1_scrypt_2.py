s = int(input("Введите количество секунд: "))
m = s // 60
h = s // 3600
while m > 60:
	m = m - 60
	h = h + 1
s = s % 60
my_str = f'введенное время: {h:02} : {m:02} : {s:02}'
print(my_str)