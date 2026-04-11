# Переписать код лабораторных работ 7 и 8 с использованием классов.
# Лабораторная работа 7, задание 3 — ряд Тейлора для ln((1+x)/(1-x)) (turtle).

import turtle
import math
from base_plotter import BasePlotter


class TaylorSeriesPlotter(BasePlotter):
    """Класс для построения графика ряда Тейлора и точной функции"""

    def __init__(self, eps=0.1):
        super().__init__()

        self.eps = eps
        self.x_start = -0.99
        self.x_end = 0.99
        self.step = 0.01

    def calculate_ln_taylor(self, x):
        """Вычисление ln((1+x)/(1-x)) через ряд Тейлора"""
        if abs(x) >= 1:
            return None, 0

        n = 0
        sum_val = 0
        term = 1

        while abs(term) > self.eps and n < 1000:
            term = (x ** (2 * n + 1)) / (2 * n + 1)
            sum_val += 2 * term  # Умножаем на 2 для ln((1+x)/(1-x))
            n += 1

        return sum_val, n

    def setup_coordinate_system(self):
        """Настройка системы координат"""
        self.setup_screen(1000, 700, (-1.1, -4, 1.1, 4),
                          "Ряд Тейлора для ln((1+x)/(1-x)) - Лабораторная работа 7")

        self.draw_axes(-1, 1, -3.5, 3.5)
        self.draw_axis_labels((0.9, -0.3), (0.1, 3.3))

        # Разметка оси X
        self.draw_x_ticks([-1, -0.5, 0.5, 1], tick_size=0.1, label_offset=(-0.05, -0.3))

        # Разметка оси Y
        self.draw_y_ticks([-3, -2, -1, 1, 2, 3], tick_size=0.05, label_offset=(0.1, -0.1))

        self.finish_axes()

    def plot_functions(self):
        """Построение графиков ряда Тейлора и эталонной функции"""
        self.setup_coordinate_system()

        # Черепашка для ряда Тейлора
        taylor_turtle = turtle.Turtle()
        taylor_turtle.speed(0)
        taylor_turtle.color("blue")
        taylor_turtle.width(2)

        # Черепашка для точной функции
        exact_turtle = turtle.Turtle()
        exact_turtle.speed(0)
        exact_turtle.color("red")
        exact_turtle.width(2)

        # Построение ряда Тейлора
        taylor_turtle.penup()
        first_point_taylor = True
        x = self.x_start

        while x <= self.x_end:
            y_taylor, iterations = self.calculate_ln_taylor(x)

            if y_taylor is not None:
                if first_point_taylor:
                    taylor_turtle.goto(x, y_taylor)
                    taylor_turtle.pendown()
                    first_point_taylor = False
                else:
                    taylor_turtle.goto(x, y_taylor)

            x += self.step

        # Построение точной функции
        exact_turtle.penup()
        first_point_exact = True
        x = self.x_start

        while x <= self.x_end:
            if abs(x) < 1:
                y_exact = math.log((1 + x) / (1 - x))

                if first_point_exact:
                    exact_turtle.goto(x, y_exact)
                    exact_turtle.pendown()
                    first_point_exact = False
                else:
                    exact_turtle.goto(x, y_exact)

            x += self.step

        taylor_turtle.hideturtle()
        exact_turtle.hideturtle()

        # Вывод информации
        info_turtle = turtle.Turtle()
        info_turtle.penup()
        info_turtle.goto(-1, 3.7)
        info_turtle.color("darkblue")
        info_turtle.write("Ряд Тейлора для ln((1+x)/(1-x))", font=("Arial", 12, "bold"))
        info_turtle.goto(-1, 3.5)
        info_turtle.write("Синий: ряд Тейлора", font=("Arial", 10))
        info_turtle.goto(-1, 3.3)
        info_turtle.write("Красный: точная функция", font=("Arial", 10))
        info_turtle.goto(-1, 3.1)
        info_turtle.write(f"Точность ε = {self.eps}", font=("Arial", 10))
        info_turtle.hideturtle()


def main():
    plotter = TaylorSeriesPlotter(eps=0.1)
    plotter.plot_functions()
    turtle.mainloop()


if __name__ == "__main__":
    main()
