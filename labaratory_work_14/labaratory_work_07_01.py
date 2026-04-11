# Переписать код лабораторных работ 7 и 8 с использованием классов.
# Лабораторная работа 7, задание 1 — график кусочной функции (turtle).

import turtle
import math
from base_plotter import BasePlotter


class FunctionPlotter(BasePlotter):
    """Класс для построения графика кусочной функции"""

    def __init__(self):
        super().__init__()

        # Параметры области отображения
        self.x_start = -4
        self.x_end = 10
        self.step = 0.1

        self.graph_turtle = None

    def calculate_function(self, x):
        """Вычисление значения кусочной функции"""
        if x < -4 or x > 10:
            return None

        if x <= -2:
            return x + 3
        elif x <= 4:
            return -0.5 * x
        elif x <= 6:
            return -2
        else:  # 6 < x <= 10
            return math.sqrt(4 - (x - 8) ** 2) - 2

    def setup_coordinate_system(self):
        """Настройка системы координат"""
        self.setup_screen(1000, 700, (-6, -5, 12, 4),
                          "График кусочной функции - Лабораторная работа 7")

        self.draw_axes(-5, 11, -4, 3)
        self.draw_axis_labels((10.5, -0.5), (0.5, 2.8))

        # Разметка оси X
        self.draw_x_ticks(range(-4, 11, 2), tick_size=0.2, label_offset=(-0.2, -0.5))

        # Разметка оси Y
        self.draw_y_ticks(range(-4, 4), tick_size=0.2, label_offset=(0.5, -0.1))

        self.finish_axes()

    def plot_function(self):
        """Построение графика функции"""
        # Настройка системы координат
        self.setup_coordinate_system()

        # Черепашка для графика
        self.graph_turtle = turtle.Turtle()
        self.graph_turtle.speed(0)
        self.graph_turtle.color("blue")
        self.graph_turtle.width(3)

        # Построение графика
        first_point = True
        x = self.x_start

        while x <= self.x_end:
            y = self.calculate_function(x)

            if y is not None:
                if first_point:
                    self.graph_turtle.penup()
                    self.graph_turtle.goto(x, y)
                    self.graph_turtle.pendown()
                    first_point = False
                else:
                    self.graph_turtle.goto(x, y)
            else:
                first_point = True

            x += self.step

        self.graph_turtle.hideturtle()

        # Вывод информации о функции
        info_turtle = turtle.Turtle()
        info_turtle.penup()
        info_turtle.goto(-5, 3.5)
        info_turtle.color("darkblue")
        info_turtle.write("График кусочной функции:", font=("Arial", 12, "bold"))
        info_turtle.goto(-5, 3.2)
        info_turtle.write("• x ∈ [-4, -2]: y = x + 3", font=("Arial", 10))
        info_turtle.goto(-5, 3.0)
        info_turtle.write("• x ∈ [-2, 4]: y = -0.5x", font=("Arial", 10))
        info_turtle.goto(-5, 2.8)
        info_turtle.write("• x ∈ [4, 6]: y = -2", font=("Arial", 10))
        info_turtle.goto(-5, 2.6)
        info_turtle.write("• x ∈ [6, 10]: y = √(4 - (x-8)²) - 2", font=("Arial", 10))
        info_turtle.hideturtle()


def main():
    plotter = FunctionPlotter()
    plotter.plot_function()
    turtle.mainloop()


if __name__ == "__main__":
    main()
