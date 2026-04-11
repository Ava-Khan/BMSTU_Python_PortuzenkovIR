# Базовый класс для построения графиков с помощью turtle.
# Содержит общие методы настройки окна и рисования осей.

import turtle


class BasePlotter:
    """Базовый класс с общими методами настройки окна и осей"""

    def __init__(self):
        self.screen = None
        self.axis_turtle = None

    def setup_screen(self, width, height, world_coords, title):
        """Настройка окна и создание черепашки для осей"""
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.setworldcoordinates(*world_coords)
        self.screen.bgcolor("white")
        self.screen.title(title)

        # Черепашка для осей
        self.axis_turtle = turtle.Turtle()
        self.axis_turtle.speed(0)
        self.axis_turtle.color("black")
        self.axis_turtle.width(2)

    def draw_axes(self, x_from, x_to, y_from, y_to):
        """Рисование осей X и Y"""
        # Рисование оси X
        self.axis_turtle.penup()
        self.axis_turtle.goto(x_from, 0)
        self.axis_turtle.pendown()
        self.axis_turtle.goto(x_to, 0)

        # Рисование оси Y
        self.axis_turtle.penup()
        self.axis_turtle.goto(0, y_from)
        self.axis_turtle.pendown()
        self.axis_turtle.goto(0, y_to)

    def draw_axis_labels(self, x_label_pos, y_label_pos):
        """Подписи осей X и Y"""
        self.axis_turtle.penup()
        self.axis_turtle.goto(*x_label_pos)
        self.axis_turtle.write("X")
        self.axis_turtle.goto(*y_label_pos)
        self.axis_turtle.write("Y")

    def draw_x_ticks(self, ticks, tick_size, label_offset):
        """Разметка оси X: ticks — список значений, tick_size — размер засечки, label_offset — смещение подписи"""
        for x in ticks:
            self.axis_turtle.penup()
            self.axis_turtle.goto(x, -tick_size)
            self.axis_turtle.pendown()
            self.axis_turtle.goto(x, tick_size)
            self.axis_turtle.penup()
            self.axis_turtle.goto(x + label_offset[0], label_offset[1])
            self.axis_turtle.write(str(x))

    def draw_y_ticks(self, ticks, tick_size, label_offset):
        """Разметка оси Y: ticks — список значений, tick_size — размер засечки, label_offset — смещение подписи"""
        for y in ticks:
            self.axis_turtle.penup()
            self.axis_turtle.goto(-tick_size, y)
            self.axis_turtle.pendown()
            self.axis_turtle.goto(tick_size, y)
            self.axis_turtle.penup()
            self.axis_turtle.goto(label_offset[0], y + label_offset[1])
            self.axis_turtle.write(str(y))

    def finish_axes(self):
        """Скрытие черепашки осей"""
        self.axis_turtle.hideturtle()
