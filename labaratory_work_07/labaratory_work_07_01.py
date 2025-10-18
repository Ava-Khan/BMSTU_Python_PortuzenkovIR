import turtle
import math


def calculate_function(x):
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


def setup_coordinate_system():
    """Настройка системы координат"""
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.setworldcoordinates(-6, -5, 12, 4)
    screen.bgcolor("white")
    screen.title("График кусочной функции - Лабораторная работа 3")

    # Настройка черепашки для осей
    axis_turtle = turtle.Turtle()
    axis_turtle.speed(0)
    axis_turtle.color("black")
    axis_turtle.width(2)

    # Рисование осей
    axis_turtle.penup()
    axis_turtle.goto(-5, 0)
    axis_turtle.pendown()
    axis_turtle.goto(11, 0)  # Ось X

    axis_turtle.penup()
    axis_turtle.goto(0, -4)
    axis_turtle.pendown()
    axis_turtle.goto(0, 3)  # Ось Y

    # Подписи осей
    axis_turtle.penup()
    axis_turtle.goto(10.5, -0.5)
    axis_turtle.write("X")
    axis_turtle.goto(0.5, 2.8)
    axis_turtle.write("Y")

    # Разметка осей
    for x in range(-4, 11, 2):
        axis_turtle.penup()
        axis_turtle.goto(x, -0.2)
        axis_turtle.pendown()
        axis_turtle.goto(x, 0.2)
        axis_turtle.penup()
        axis_turtle.goto(x - 0.2, -0.5)
        axis_turtle.write(str(x))

    for y in range(-4, 4):
        axis_turtle.penup()
        axis_turtle.goto(-0.2, y)
        axis_turtle.pendown()
        axis_turtle.goto(0.2, y)
        axis_turtle.penup()
        axis_turtle.goto(0.5, y - 0.1)
        axis_turtle.write(str(y))

    axis_turtle.hideturtle()
    return axis_turtle


def plot_function():
    """Построение графика функции"""
    # Настройка системы координат
    setup_coordinate_system()

    # Черепашка для графика
    graph_turtle = turtle.Turtle()
    graph_turtle.speed(0)
    graph_turtle.color("blue")
    graph_turtle.width(3)

    # Параметры построения
    x_start = -4
    x_end = 10
    step = 0.1

    # Построение графика
    first_point = True

    x = x_start
    while x <= x_end:
        y = calculate_function(x)

        if y is not None:
            if first_point:
                graph_turtle.penup()
                graph_turtle.goto(x, y)
                graph_turtle.pendown()
                first_point = False
            else:
                graph_turtle.goto(x, y)
        else:
            first_point = True

        x += step

    graph_turtle.hideturtle()

    # Вывод информации
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
    plot_function()
    turtle.mainloop()


if __name__ == "__main__":
    main()