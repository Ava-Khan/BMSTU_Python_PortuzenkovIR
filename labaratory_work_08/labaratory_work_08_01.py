from tkinter import *
from tkinter.messagebox import askyesno
import math


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


# Создаем главное окно
root = Tk()
root.title("Графики функций - Вариант 5")
root.resizable(False, False)

# Параметры полотна (70% от экрана)
Kp = 0.7
MaxX = int(root.winfo_screenwidth() * Kp)
MaxY = int(root.winfo_screenheight() * Kp)

# Создаем холст
cv = Canvas(root, width=MaxX, height=MaxY, bg="white")
cv.grid(row=0, columnspan=9)

# Глобальные переменные
Xmin, Xmax = -2.0, 2.0  # Границы по X (ограничены для сходимости ряда)
Ymin, Ymax = -2.0, 2.0  # Границы по Y
dX, dY = 0.5, 0.0  # Шаг и смещение
Kx = MaxX / (Xmax - Xmin) if (Xmax - Xmin) != 0 else 1
Ky = MaxY / (Ymax - Ymin) if (Ymax - Ymin) != 0 else 1
ID1, ID2 = 0, 0


def GetData():
    """Обновляет глобальные переменные из полей ввода"""
    global Xmin, Xmax, Ymin, Ymax, dX, dY, Kx, Ky

    try:
        Xmin = float(entries[2].get())
        Xmax = float(entries[3].get())
        Ymin = float(entries[4].get())
        Ymax = float(entries[5].get())
        dX = float(entries[6].get())
        dY = float(entries[7].get())

        # Пересчитываем масштабные коэффициенты
        Kx = MaxX / (Xmax - Xmin) if (Xmax - Xmin) != 0 else 1
        Ky = MaxY / (Ymax - Ymin) if (Ymax - Ymin) != 0 else 1

    except ValueError:
        print("Ошибка ввода данных!")


def DrawAxes():
    """Рисует координатные оси и разметку"""
    # Горизонтальная ось X (y=0)
    y_zero = MaxY - Ky * (0 - Ymin)
    if Ymin <= 0 <= Ymax:
        cv.create_line(0, y_zero, MaxX, y_zero, fill="black", width=2)

    # Вертикальная ось Y (x=0)
    x_zero = Kx * (0 - Xmin)
    if Xmin <= 0 <= Xmax:
        cv.create_line(x_zero, 0, x_zero, MaxY, fill="black", width=2)

    # Разметка оси X
    x = Xmin
    while x <= Xmax:
        if abs(x) > 0.1:  # Не рисуем слишком близко к нулю
            x_pixel = Kx * (x - Xmin)
            cv.create_line(x_pixel, y_zero - 5, x_pixel, y_zero + 5, fill="black")
            cv.create_text(x_pixel, y_zero + 15, text=f"{x:.1f}", anchor=N)
        x += dX

    # Разметка оси Y
    y = Ymin
    while y <= Ymax:
        if abs(y) > 0.1:  # Не рисуем слишком близко к нулю
            y_pixel = MaxY - Ky * (y - Ymin)
            cv.create_line(x_zero - 5, y_pixel, x_zero + 5, y_pixel, fill="black")
            cv.create_text(x_zero - 10, y_pixel, text=f"{y:.1f}", anchor=E)
        y += dX


def DrawFunction(func, color, name):
    """Рисует график функции"""
    points = []
    x = Xmin
    step = (Xmax - Xmin) / 1000  # 1000 точек для плавности

    while x <= Xmax:
        try:
            y = func(x)
            if y is not None and Ymin <= y <= Ymax:
                x_pixel = Kx * (x - Xmin)
                y_pixel = MaxY - Ky * (y - Ymin)
                points.append((x_pixel, y_pixel))
            else:
                # Если точка вне диапазона, начинаем новую линию
                if len(points) > 1:
                    cv.create_line(points, fill=color, width=2)
                points = []
        except:
            points = []  # Начинаем новую линию при ошибке
        x += step

    # Рисуем последнюю линию
    if len(points) > 1:
        cv.create_line(points, fill=color, width=2, smooth=True)


def Draw(event):
    """Рисует графики функций"""
    # Получаем данные из полей ввода
    GetData()

    # Очищаем холст
    cv.delete("all")

    # Рисуем координатные оси
    DrawAxes()

    # Получаем смещение b из поля ввода
    try:
        b = float(entries[7].get())  # поле "Смещение"
    except:
        b = 0.0

    # Рисуем графики
    DrawFunction(taylor_arctan, "blue", "Ряд Тейлора (arctg)")
    DrawFunction(lambda x: analytic_arctan(x, b), "red", "Аналитическая (arctg + b)")

    # Добавляем легенду
    cv.create_text(10, 20, text="Синий: Ряд Тейлора", anchor=NW, fill="blue", font=("Arial", 10))
    cv.create_text(10, 40, text="Красный: arctg(x) + b", anchor=NW, fill="red", font=("Arial", 10))

    print("Графики построены!")


def Final(event):
    """Завершает работу программы"""
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


def showXY(event):
    """Показывает координаты точки на холсте"""
    global ID1, ID2
    x = event.x
    y = event.y

    # Преобразуем координаты пикселей в математические
    x_math = Xmin + x / Kx
    y_math = Ymin + (MaxY - y) / Ky

    # Обновляем поля ввода
    entries[0].delete(0, END)
    entries[0].insert(0, f"{x_math:.2f}")
    entries[1].delete(0, END)
    entries[1].insert(0, f"{y_math:.2f}")

    # Рисуем перекрестие
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5), fill="gray")
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5), fill="gray")


def window_deleted():
    """Обрабатывает закрытие окна через [X]"""
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


# Привязка обработчиков событий
cv.bind('<Button-1>', showXY)
root.protocol('WM_DELETE_WINDOW', window_deleted)

# Создаем метки и поля ввода
labels_text = ["X:", "Y:", "Xmin:", "Xmax:", "Ymin:", "Ymax:", "Шаг меток:", "Смещение:"]
entries = []

for i, text in enumerate(labels_text):
    # Метки
    lbl = Label(root, text=text, width=10, fg="blue", font=("Ubuntu", 12))
    lbl.grid(row=1 + i % 2, column=(i // 2) * 2, sticky='e', padx=5, pady=2)

    # Поля ввода
    ent = Entry(root, width=8, font=("Ubuntu", 12))
    ent.grid(row=1 + i % 2, column=(i // 2) * 2 + 1, padx=5, pady=2)
    entries.append(ent)

# Заполняем поля начальными значениями
initial_values = ["0.00", "0.00", "-2.0", "2.0", "-2.0", "2.0", "0.5", "0.0"]
for ent, val in zip(entries, initial_values):
    ent.delete(0, END)
    ent.insert(0, str(val))

# Кнопки
btn1 = Button(root, width=20, bg="#ccc", text="Рисовать", font=("Ubuntu", 10))
btn1.grid(row=1, column=8, padx=10, pady=5)
btn1.bind("<Button-1>", Draw)

btn2 = Button(root, width=20, bg="#ccc", text="Выход", font=("Ubuntu", 10))
btn2.grid(row=2, column=8, padx=10, pady=5)
btn2.bind("<Button-1>", Final)

# Запуск главного цикла
print("Программа запущена! Нажмите 'Рисовать' для построения графиков.")
print("Синий график - ряд Тейлора для arctg(x) (|x| ≤ 1)")
print("Красный график - аналитическая функция arctg(x) + b")
root.mainloop()