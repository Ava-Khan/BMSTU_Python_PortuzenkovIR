import turtle
import random
import math

turtle.tracer(1)
def check_hit(x, y, r):
    """Проверка попадания точки в заштрихованную область"""
    in_first_quarter = x >= 0 and y >= 0 and math.sqrt(x ** 2 + y ** 2) <= r
    in_third_quarter = x <= 0 and y <= 0 and math.sqrt(x ** 2 + y ** 2) <= r
    in_second_quarter = x <= 0 and y >= 0 and y <= x + r

    return in_first_quarter or in_third_quarter or in_second_quarter


def fill_circular_segment(turtle_obj, center_x, center_y, radius, start_angle, end_angle, steps=100):
    """Точная заливка сегмента окружности"""
    turtle_obj.penup()
    turtle_obj.goto(center_x, center_y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()

    angle_step = (end_angle - start_angle) / steps
    for i in range(steps + 1):
        angle = math.radians(start_angle + i * angle_step)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        turtle_obj.goto(x, y)

    turtle_obj.goto(center_x, center_y)
    turtle_obj.end_fill()


def setup_coordinate_system(r):
    """Настройка системы координат с точной заливкой"""
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.setworldcoordinates(-r - 1, -r - 1, r + 1, r + 1)
    screen.bgcolor("white")
    screen.title(f"Метод Монте-Карло (r = {r}) - Лабораторная работа 3")

    axis_turtle = turtle.Turtle()
    axis_turtle.speed(0)
    axis_turtle.color("black")
    axis_turtle.width(2)

    axis_turtle.penup()
    axis_turtle.goto(-r, 0)
    axis_turtle.pendown()
    axis_turtle.goto(r, 0)

    axis_turtle.penup()
    axis_turtle.goto(0, -r)
    axis_turtle.pendown()
    axis_turtle.goto(0, r)

    axis_turtle.penup()
    axis_turtle.goto(0, -r)
    axis_turtle.pendown()
    axis_turtle.circle(r)

    axis_turtle.penup()
    axis_turtle.goto(-r, 0)
    axis_turtle.pendown()
    axis_turtle.goto(0, r)

    fill_turtle = turtle.Turtle()
    fill_turtle.speed(0)
    fill_turtle.color("lightblue")
    fill_turtle.width(1)

    fill_circular_segment(fill_turtle, 0, 0, r, 0, 90)
    fill_circular_segment(fill_turtle, 0, 0, r, 180, 270)

    fill_turtle.color("lightgreen")
    fill_turtle.penup()
    fill_turtle.goto(-r, 0)
    fill_turtle.pendown()
    fill_turtle.begin_fill()

    steps = 50
    for i in range(steps + 1):
        angle = math.radians(180 - i * 90 / steps)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        fill_turtle.goto(x, y)

    fill_turtle.goto(-r, 0)
    fill_turtle.end_fill()

    fill_turtle.hideturtle()
    axis_turtle.hideturtle()

    return axis_turtle


def calculate_theoretical_area(r):
    """Точное вычисление теоретической площади"""
    area_first_quarter = (math.pi * r ** 2) / 4
    area_third_quarter = (math.pi * r ** 2) / 4
    area_second_quarter_circle = (math.pi * r ** 2) / 4
    area_triangle_under_line = 0.5 * r * r
    area_second_quarter = area_second_quarter_circle - area_triangle_under_line

    total_area = area_first_quarter + area_second_quarter + area_third_quarter
    return total_area


def monte_carlo_simulation(r, num_points=5000):
    """Моделирование методом Монте-Карло"""
    setup_coordinate_system(r)

    hit_turtle = turtle.Turtle()
    hit_turtle.speed(0)
    hit_turtle.color("red")
    hit_turtle.shape("circle")
    hit_turtle.shapesize(0.2)

    miss_turtle = turtle.Turtle()
    miss_turtle.speed(0)
    miss_turtle.color("darkgray")
    miss_turtle.shape("circle")
    miss_turtle.shapesize(0.15)

    hit_count = 0

    for i in range(num_points):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        if check_hit(x, y, r):
            hit_turtle.penup()
            hit_turtle.goto(x, y)
            hit_turtle.stamp()
            hit_count += 1
        else:
            miss_turtle.penup()
            miss_turtle.goto(x, y)
            miss_turtle.stamp()

    square_area = (2 * r) ** 2
    estimated_area = (hit_count / num_points) * square_area
    theoretical_area = calculate_theoretical_area(r)

    result_turtle = turtle.Turtle()
    result_turtle.penup()
    result_turtle.goto(-r, r + 0.8)
    result_turtle.color("darkblue")

    result_turtle.write(f"Метод Монте-Карло (N = {num_points})",
                        font=("Arial", 12, "bold"))
    result_turtle.goto(-r, r + 0.5)
    result_turtle.write(f"Попаданий: {hit_count}/{num_points} ({hit_count / num_points * 100:.1f}%)",
                        font=("Arial", 10))
    result_turtle.goto(-r, r + 0.2)
    result_turtle.write(f"Оценка площади: {estimated_area:.4f}",
                        font=("Arial", 10))
    result_turtle.goto(-r, r - 0.1)
    result_turtle.write(f"Теоретическая площадь: {theoretical_area:.4f}",
                        font=("Arial", 10))
    result_turtle.goto(-r, r - 0.4)
    error = abs(estimated_area - theoretical_area)
    accuracy = (1 - error / theoretical_area) * 100
    result_turtle.write(f"Погрешность: {error:.4f} ({accuracy:.1f}% точности)",
                        font=("Arial", 10, "bold"))

    result_turtle.goto(-r, r - 0.7)
    result_turtle.write("Легенда:", font=("Arial", 10, "bold"))
    result_turtle.goto(-r, r - 0.9)
    result_turtle.write("• Светло-синий: 1-я и 3-я четверти круга", font=("Arial", 8))
    result_turtle.goto(-r, r - 1.1)
    result_turtle.write("• Светло-зеленый: 2-я четверть", font=("Arial", 8))
    result_turtle.goto(-r, r - 1.3)
    result_turtle.write("• Красные точки: попадания в область", font=("Arial", 8))
    result_turtle.goto(-r, r - 1.5)
    result_turtle.write("• Серые точки: промахи", font=("Arial", 8))

    result_turtle.hideturtle()

    return estimated_area, theoretical_area, accuracy


def main():
    r = 5
    monte_carlo_simulation(r, 10000)
    turtle.mainloop()


if __name__ == "__main__":
    main()