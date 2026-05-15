import ctypes
import sys


class MyList:
    def __init__(self):
        self.length = 0  # Текущее количество элементов в списке
        self.capacity = 8  # Выделенный объем памяти
        self.array = (self.capacity * ctypes.py_object)()

    def append(self, item):
        """Добавление элемента в самый конец списка"""
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = item
        self.length += 1

    def pop(self):
        """Удаление последнего элемента из списка"""
        if self.length == 0:
            raise IndexError("Попытка удалить элемент из пустого списка")
        self.length -= 1
        if self.length <= (self.capacity // 2 + 1) and self.capacity > 8:
            self._resize(self.capacity // 2 + 1)

    def insert(self, index, item):
        """Вставка элемента в произвольное место по индексу"""
        # Корректировка отрицательного индекса
        if index < 0:
            index = max(0, self.length + index)
        # Если индекс больше длины, отправляем элемент в конец
        if index > self.length:
            index = self.length

        # Если в выделенной памяти не осталось места расширяем ее
        if self.length == self.capacity:
            self._resize(self.capacity * 2)

        # Сдвигаем элементы вправо, чтобы освободить место для нового элемента
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        # Записываем элемент и увеличиваем длину
        self.array[index] = item
        self.length += 1

    def remove_at(self, index):
        """Удаление элемента из произвольного места по индексу"""
        # Корректировка отрицательного индекса
        if index < 0:
            index = self.length + index

        # Проверка, что индекс вообще существует
        if index < 0 or index >= self.length:
            raise IndexError("Индекс находится за пределами списка")

        # Сдвигаем элементы влево, затирая удаляемый элемент
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.length -= 1

        # Оптимизация памяти
        if self.length <= (self.capacity // 2 + 1) and self.capacity > 8:
            self._resize(self.capacity // 2 + 1)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Индекс находится за пределами списка")
        return self.array[index]

    def _resize(self, new_capacity):
        new_array = (new_capacity * ctypes.py_object)()
        for index in range(self.length):
            new_array[index] = self.array[index]
        self.array = new_array
        self.capacity = new_capacity

    def display(self):
        """Возвращает обычный список для удобного вывода в консоль"""
        return [self.array[i] for i in range(self.length)]



if __name__ == "__main__":
    my_list = MyList()

    print("1. Заполняем начальный список элементами:")
    my_list.append("один")
    my_list.append("два")
    my_list.append("три")
    print(
        f"Текущий список: {my_list.display()}, Занято ячеек: {len(my_list)}, Всего памяти выделено: {my_list.capacity}")
    print("-" * 60)

    print("2. Вставляем новый элемент на позицию с индексом 1 (в середину):")
    my_list.insert(1, "ВСТАВЛЕННЫЙ_ЭЛЕМЕНТ")
    print(f"Список после вставки: {my_list.display()}")
    print(f"Занято ячеек: {len(my_list)}, Всего памяти выделено: {my_list.capacity}")
    print("-" * 60)

    print("3. Удаляем элемент из произвольного места (с индексом 2):")
    my_list.remove_at(2)
    print(f"Список после удаления по индексу: {my_list.display()}")
    print("-" * 60)

    print("4. Удаляем элемент с конца списка:")
    my_list.pop()
    print(f"Итоговый список: {my_list.display()}")
    print(f"Занято ячеек: {len(my_list)}, Всего памяти выделено: {my_list.capacity}")