# Базовый класс для tkinter-приложений с графиком функции.
# Содержит общие методы настройки окна, холста, осей и отображения координат.

from tkinter import *
from tkinter.messagebox import askyesno


class BaseGraphApp:
    """Базовый класс tkinter-приложения для построения графиков"""

    def __init__(self, title):
        # Создаем главное окно
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)

        # Параметры полотна (70% от экрана)
        Kp = 0.7
        self.MaxX = int(self.root.winfo_screenwidth() * Kp)
        self.MaxY = int(self.root.winfo_screenheight() * Kp)

        # Создаем холст
        self.cv = Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, columnspan=9)

        # Параметры отображения
        self.Xmin = -2.0
        self.Xmax = 2.0
        self.Ymin = -2.0
        self.Ymax = 2.0
        self.dX = 0.5

        # Масштабные коэффициенты
        self.Kx = self.MaxX / (self.Xmax - self.Xmin)
        self.Ky = self.MaxY / (self.Ymax - self.Ymin)

        # Идентификаторы линий перекрестия
        self.ID1 = 0
        self.ID2 = 0

    def update_scale(self):
        """Пересчёт масштабных коэффициентов"""
        self.Kx = self.MaxX / (self.Xmax - self.Xmin) if (self.Xmax - self.Xmin) != 0 else 1
        self.Ky = self.MaxY / (self.Ymax - self.Ymin) if (self.Ymax - self.Ymin) != 0 else 1

    def draw_axes(self):
        """Рисует координатные оси и разметку"""
        # Горизонтальная ось X (y=0)
        y_zero = self.MaxY - self.Ky * (0 - self.Ymin)
        if self.Ymin <= 0 <= self.Ymax:
            self.cv.create_line(0, y_zero, self.MaxX, y_zero, fill="black", width=2)

        # Вертикальная ось Y (x=0)
        x_zero = self.Kx * (0 - self.Xmin)
        if self.Xmin <= 0 <= self.Xmax:
            self.cv.create_line(x_zero, 0, x_zero, self.MaxY, fill="black", width=2)

        # Разметка оси X
        x = self.Xmin
        while x <= self.Xmax:
            if abs(x) > 0.1:  # Не рисуем слишком близко к нулю
                x_pixel = self.Kx * (x - self.Xmin)
                y_zero = self.MaxY - self.Ky * (0 - self.Ymin)
                self.cv.create_line(x_pixel, y_zero - 5, x_pixel, y_zero + 5, fill="black")
                self.cv.create_text(x_pixel, y_zero + 15, text=f"{x:.1f}", anchor=N)
            x += self.dX

        # Разметка оси Y
        x_zero = self.Kx * (0 - self.Xmin)
        y = self.Ymin
        while y <= self.Ymax:
            if abs(y) > 0.1:  # Не рисуем слишком близко к нулю
                y_pixel = self.MaxY - self.Ky * (y - self.Ymin)
                self.cv.create_line(x_zero - 5, y_pixel, x_zero + 5, y_pixel, fill="black")
                self.cv.create_text(x_zero - 10, y_pixel, text=f"{y:.1f}", anchor=E)
            y += self.dX

    def draw_function(self, func, color):
        """Рисует график функции"""
        points = []
        x = self.Xmin
        step = (self.Xmax - self.Xmin) / 1000  # 1000 точек для плавности

        while x <= self.Xmax:
            try:
                y = func(x)
                if y is not None and self.Ymin <= y <= self.Ymax:
                    x_pixel = self.Kx * (x - self.Xmin)
                    y_pixel = self.MaxY - self.Ky * (y - self.Ymin)
                    points.append((x_pixel, y_pixel))
                else:
                    # Если точка вне диапазона, начинаем новую линию
                    if len(points) > 1:
                        self.cv.create_line(points, fill=color, width=2)
                    points = []
            except:
                points = []  # Начинаем новую линию при ошибке
            x += step

        # Рисуем последнюю линию
        if len(points) > 1:
            self.cv.create_line(points, fill=color, width=2, smooth=True)

    def show_xy(self, event, entries):
        """Показывает координаты точки на холсте"""
        x = event.x
        y = event.y

        # Преобразуем координаты пикселей в математические
        x_math = self.Xmin + x / self.Kx
        y_math = self.Ymin + (self.MaxY - y) / self.Ky

        # Обновляем поля ввода
        entries[0].delete(0, END)
        entries[0].insert(0, f"{x_math:.2f}")
        entries[1].delete(0, END)
        entries[1].insert(0, f"{y_math:.2f}")

        # Рисуем перекрестие
        self.cv.delete(self.ID1)
        self.cv.delete(self.ID2)
        self.ID1 = self.cv.create_line(0, y, self.MaxX, y, dash=(3, 5), fill="gray")
        self.ID2 = self.cv.create_line(x, 0, x, self.MaxY, dash=(3, 5), fill="gray")

    def window_deleted(self):
        """Обрабатывает закрытие окна через [X]"""
        if askyesno("Выход", "Завершить работу?"):
            self.root.destroy()

    def run(self):
        """Запуск главного цикла"""
        self.root.mainloop()
