# Переписать код лабораторных работ 7 и 8 с использованием классов.
# Лабораторная работа 8, задание 1 — графики функций (tkinter).

from tkinter import *
from tkinter.messagebox import askyesno
import math
from base_graph_app import BaseGraphApp


# Функции вычисления для 5 варианта
def taylor_arctan(x, epsilon=0.0001):
    if abs(x) > 1:
        return None

    result = 0
    term = x
    n = 0

    while abs(term) > epsilon:
        result += term
        n += 1
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)

    return result


def analytic_arctan(x, b):
    """Вычисляет arctg(x) + b"""
    return math.atan(x) + b


class GraphApp(BaseGraphApp):
    """Класс приложения для построения графиков arctg(x) — вариант 5"""

    def __init__(self):
        super().__init__("Графики функций - Вариант 5")

        # Поля ввода
        self.entries = []

        self._build_ui()
        self._bind_events()

    def _build_ui(self):
        """Создание элементов интерфейса"""
        # Метки и поля ввода
        labels_text = ["X:", "Y:", "Xmin:", "Xmax:", "Ymin:", "Ymax:", "Шаг меток:", "Смещение:"]

        for i, text in enumerate(labels_text):
            # Метки
            lbl = Label(self.root, text=text, width=10, fg="blue", font=("Ubuntu", 12))
            lbl.grid(row=1 + i % 2, column=(i // 2) * 2, sticky='e', padx=5, pady=2)

            # Поля ввода
            ent = Entry(self.root, width=8, font=("Ubuntu", 12))
            ent.grid(row=1 + i % 2, column=(i // 2) * 2 + 1, padx=5, pady=2)
            self.entries.append(ent)

        # Заполняем поля начальными значениями
        initial_values = ["0.00", "0.00", "-2.0", "2.0", "-2.0", "2.0", "0.5", "0.0"]
        for ent, val in zip(self.entries, initial_values):
            ent.delete(0, END)
            ent.insert(0, str(val))

        # Кнопки
        btn1 = Button(self.root, width=20, bg="#ccc", text="Рисовать", font=("Ubuntu", 10))
        btn1.grid(row=1, column=8, padx=10, pady=5)
        btn1.bind("<Button-1>", self.draw)

        btn2 = Button(self.root, width=20, bg="#ccc", text="Выход", font=("Ubuntu", 10))
        btn2.grid(row=2, column=8, padx=10, pady=5)
        btn2.bind("<Button-1>", self.final)

    def _bind_events(self):
        """Привязка обработчиков событий"""
        self.cv.bind('<Button-1>', lambda e: self.show_xy(e, self.entries))
        self.root.protocol('WM_DELETE_WINDOW', self.window_deleted)

    def get_data(self):
        """Обновляет параметры из полей ввода"""
        try:
            self.Xmin = float(self.entries[2].get())
            self.Xmax = float(self.entries[3].get())
            self.Ymin = float(self.entries[4].get())
            self.Ymax = float(self.entries[5].get())
            self.dX = float(self.entries[6].get())

            # Пересчитываем масштабные коэффициенты
            self.update_scale()

        except ValueError:
            print("Ошибка ввода данных!")

    def draw(self, event):
        """Рисует графики функций"""
        # Получаем данные из полей ввода
        self.get_data()

        # Очищаем холст
        self.cv.delete("all")

        # Рисуем координатные оси
        self.draw_axes()

        # Получаем смещение b из поля ввода
        try:
            b = float(self.entries[7].get())  # поле "Смещение"
        except:
            b = 0.0

        # Рисуем графики
        self.draw_function(taylor_arctan, "blue")
        self.draw_function(lambda x: analytic_arctan(x, b), "red")

        # Добавляем легенду
        self.cv.create_text(10, 20, text="Синий: Ряд Тейлора", anchor=NW, fill="blue", font=("Arial", 10))
        self.cv.create_text(10, 40, text="Красный: arctg(x) + b", anchor=NW, fill="red", font=("Arial", 10))

        print("Графики построены!")

    def final(self, event):
        """Завершает работу программы"""
        if askyesno("Выход", "Завершить работу?"):
            self.root.destroy()

    def run(self):
        """Запуск главного цикла"""
        print("Программа запущена! Нажмите 'Рисовать' для построения графиков.")
        print("Синий график - ряд Тейлора для arctg(x) (|x| ≤ 1)")
        print("Красный график - аналитическая функция arctg(x) + b")
        super().run()


def main():
    app = GraphApp()
    app.run()


if __name__ == "__main__":
    main()
