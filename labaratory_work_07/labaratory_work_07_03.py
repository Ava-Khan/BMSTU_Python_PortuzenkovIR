import turtle
import math


def calculate_ln_taylor(x, eps=0.0001):
    """Вычисление ln((1+x)/(1-x)) через ряд Тейлора"""
    if abs(x) >= 1:
        return None, 0

    n = 0
    sum_val = 0
    term = 1

    while abs(term) > eps and n < 1000:
        term = (x ** (2 * n + 1)) / (2 * n + 1)
        sum_val += 2 * term  # Умножаем на 2 для ln((1+x)/(1-x))
        n += 1

    return sum_val, n


def setup_coordinate_system():
    """Настройка системы координат"""
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.setworldcoordinates(-1.1, -4, 1.1, 4)
    screen.bgcolor("white")
    screen.title("Ряд Тейлора для ln((1+x)/(1-x)) - Лабораторная работа 3")

    # Настройка черепашки для осей
    axis_turtle = turtle.Turtle()
    axis_turtle.speed(0)
    axis_turtle.color("black")
    axis_turtle.width(2)

    # Рисование осей
    axis_turtle.penup()
    axis_turtle.goto(-1, 0)
    axis_turtle.pendown()
    axis_turtle.goto(1, 0)  # Ось X

    axis_turtle.penup()
    axis_turtle.goto(0, -3.5)
    axis_turtle.pendown()
    axis_turtle.goto(0, 3.5)  # Ось Y

    # Подписи осей
    axis_turtle.penup()
    axis_turtle.goto(0.9, -0.3)
    axis_turtle.write("X")
    axis_turtle.goto(0.1, 3.3)
    axis_turtle.write("Y")

    # Разметка осей
    for x in [-1, -0.5, 0.5, 1]:
        axis_turtle.penup()
        axis_turtle.goto(x, -0.1)
        axis_turtle.pendown()
        axis_turtle.goto(x, 0.1)
        axis_turtle.penup()
        axis_turtle.goto(x - 0.05, -0.3)
        axis_turtle.write(str(x))

    for y in [-3, -2, -1, 1, 2, 3]:
        axis_turtle.penup()
        axis_turtle.goto(-0.05, y)
        axis_turtle.pendown()
        axis_turtle.goto(0.05, y)
        axis_turtle.penup()
        axis_turtle.goto(0.1, y - 0.1)
        axis_turtle.write(str(y))

    axis_turtle.hideturtle()
    return axis_turtle


def plot_functions():
    """Построение графиков ряда Тейлора и эталонной функции"""
    setup_coordinate_system()

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

    # Параметры построения
    x_start = -0.99
    x_end = 0.99
    step = 0.01
    eps = 0.1

    # Построение ряда Тейлора
    taylor_turtle.penup()
    first_point_taylor = True

    x = x_start
    while x <= x_end:
        y_taylor, iterations = calculate_ln_taylor(x, eps)

        if y_taylor is not None:
            if first_point_taylor:
                taylor_turtle.goto(x, y_taylor)
                taylor_turtle.pendown()
                first_point_taylor = False
            else:
                taylor_turtle.goto(x, y_taylor)

        x += step

    # Построение точной функции
    exact_turtle.penup()
    first_point_exact = True

    x = x_start
    while x <= x_end:
        if abs(x) < 1:
            y_exact = math.log((1 + x) / (1 - x))

            if first_point_exact:
                exact_turtle.goto(x, y_exact)
                exact_turtle.pendown()
                first_point_exact = False
            else:
                exact_turtle.goto(x, y_exact)

        x += step

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
    info_turtle.write(f"Точность ε = {eps}", font=("Arial", 10))
    info_turtle.hideturtle()


def main():
    plot_functions()
    turtle.mainloop()


if __name__ == "__main__":
    main()