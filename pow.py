def power(base, exponent):
	flag = exponent < 0
	if flag:
		exponent = -exponent
	result = 1
	current = base
	
	while exponent > 0:
		if exponent % 2 == 1: #если младший бит степени равен 1 - умножаем результат на current
			result = result * current

		current = current * current
		exponent = exponent // 2

	if flag:
		result = 1 / result

	return result


a = int(input("Введите основание: "))
b = int(input("Введите степень: "))

print(f"{a} в степени {b} = {power(a, b)}")
