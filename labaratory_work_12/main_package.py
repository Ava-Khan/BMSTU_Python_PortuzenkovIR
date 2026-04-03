# импорт модуля из пакета
import my_package.module_a

print("--- импорт модуля из пакета ---")
print("4! =", my_package.module_a.factorial(4))
print("Сумма цифр 1234:", my_package.module_a.digit_sum(1234))

# импорт определённых элементов из модуля в пакете
from my_package.module_b import is_palindrome, reverse_str

print("\n--- импорт конкретных элементов из модуля в пакете ---")
print("'radar' палиндром?", is_palindrome('radar'))
print("Реверс 'hello':", reverse_str('hello'))

# импорт из подпакета
from my_package.sub_package import module_c

print("\n--- импорт из подпакета ---")
print("Среднее [1,2,3,4,5]:", module_c.avg([1, 2, 3, 4, 5]))
print("Чётные из [1,2,3,4,5,6]:", module_c.filter_even([1, 2, 3, 4, 5, 6]))

# импорт конкретного элемента из подпакета
from my_package.sub_package.module_c import flatten

print("\n--- импорт конкретного элемента из подпакета ---")
print("Flatten [[1,2],[3,[4,5]]]:", flatten([[1, 2], [3, [4, 5]]]))
