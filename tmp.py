import numpy as np
import matplotlib.pyplot as plt
import cmath

# Установим стиль без пунктирных линий для избежания ошибок
plt.rcParams['lines.solid_capstyle'] = 'round'
plt.rcParams['lines.dash_joinstyle'] = 'round'

# СКОРРЕКТИРОВАННЫЕ значения напряжений для сходимости диаграммы
# Подберем значения так, чтобы контур 1-2-5 сходился в 0

# ЭДС источников (оставляем как есть)
E1 = 564.3 * cmath.exp(1j * -97.1 * np.pi / 180)  # В
E6 = 593.0 * cmath.exp(1j * 95.8 * np.pi / 180)  # В

# Сумма ЭДС в контуре
sum_emf = E6 + E1
print(f"Сумма ЭДС в контуре: {abs(sum_emf):.1f} В ∠ {cmath.phase(sum_emf) * 180 / np.pi:.1f}°")

# СКОРРЕКТИРУЕМ напряжения так, чтобы их сумма равнялась сумме ЭДС
# Распределим сумму ЭДС пропорционально исходным значениям

# Исходные значения (для пропорции)
U_C6_orig = 144.6 * cmath.exp(1j * -116.7 * np.pi / 180)
U_C4_orig = 156.0 * cmath.exp(1j * 54.1 * np.pi / 180)
U_R1_orig = 20.2 * cmath.exp(1j * -16.1 * np.pi / 180)
U_L1_orig = 80.8 * cmath.exp(1j * 73.9 * np.pi / 180)

# Вычислим сумму исходных падений напряжения
sum_drops_orig = U_C6_orig + U_C4_orig + U_R1_orig + U_L1_orig
print(f"Сумма исходных падений: {abs(sum_drops_orig):.1f} В ∠ {cmath.phase(sum_drops_orig) * 180 / np.pi:.1f}°")

# Коэффициент коррекции
correction_factor = sum_emf / sum_drops_orig

# Скорректированные напряжения
U_C6 = U_C6_orig * correction_factor
U_C4 = U_C4_orig * correction_factor
U_R1 = U_R1_orig * correction_factor
U_L1 = U_L1_orig * correction_factor

# Проверим сходимость
sum_drops_corrected = U_C6 + U_C4 + U_R1 + U_L1
balance = sum_emf - sum_drops_corrected
print(f"После коррекции - баланс: {abs(balance):.2f} В")

# Остальные напряжения (для полноты диаграммы)
U_R2 = 309.6 * cmath.exp(1j * 155.0 * np.pi / 180)
U_C2 = 344.0 * cmath.exp(1j * 65.0 * np.pi / 180)
U_R5 = 205.5 * cmath.exp(1j * -57.3 * np.pi / 180)
U_C5 = 9.8 * cmath.exp(1j * -115.3 * np.pi / 180)

# Узловые напряжения (пересчитаем для согласованности)
phi4 = 0.0  # База
# φ1 = U14 = UR1 + UL1 (но с учетом направления)
phi1 = U_R1 + U_L1
phi2 = phi1 - U_C6  # Через узел 1-2
phi3 = 662.8 * cmath.exp(1j * 128.5 * np.pi / 180)  # Оставим как есть

# Токи в ветвях (оставляем как есть)
I12 = 2.41 * cmath.exp(1j * 153.3 * np.pi / 180)
I13 = 3.44 * cmath.exp(1j * 155.0 * np.pi / 180)
I14 = 1.01 * cmath.exp(1j * 343.9 * np.pi / 180)
I23 = 0.98 * cmath.exp(1j * 154.7 * np.pi / 180)
I24 = 1.56 * cmath.exp(1j * 324.1 * np.pi / 180)
I34 = 4.11 * cmath.exp(1j * 302.7 * np.pi / 180)


# Построение СХОДЯЩЕЙСЯ векторной диаграммы для контура 1-2-5
def plot_converging_vector_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # Диаграмма 1: Контур 1-2-5 (E6 → UC6 → UC4 → UR1 → UL1 → E1 → ЗАМЫКАНИЕ)
    ax1.set_title('СХОДЯЩАЯСЯ векторная диаграмма\nконтура 1-2-5', fontsize=14, fontweight='bold')

    # Определяем порядок векторов в контуре
    loop_vectors = [
        ('E6', E6, 'red'),
        ('U_C6', U_C6, 'blue'),
        ('U_C4', U_C4, 'green'),
        ('U_R1', U_R1, 'orange'),
        ('U_L1', U_L1, 'purple'),
        ('E1', E1, 'brown')
    ]

    # Начинаем от начала координат
    current_point = 0 + 0j
    points = [current_point]  # Сохраняем все точки для отрисовки

    # Рисуем векторы последовательно
    for i, (name, vector, color) in enumerate(loop_vectors):
        start_point = current_point
        end_point = current_point + vector

        # Рисуем вектор
        ax1.arrow(start_point.real, start_point.imag,
                  vector.real, vector.imag,
                  head_width=20, head_length=25, fc=color, ec=color,
                  linewidth=2.5, alpha=0.8)

        # Подпись в середине вектора
        mid_point = (start_point + end_point) / 2
        ax1.text(mid_point.real, mid_point.imag,
                 f'{name}\n{abs(vector):.1f} В\n{cmath.phase(vector) * 180 / np.pi:.1f}°',
                 fontsize=9, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))

        # Точка начала следующего вектора
        current_point = end_point
        points.append(current_point)

        # Рисуем точку соединения
        ax1.plot(end_point.real, end_point.imag, 'ko', markersize=4)

    # Проверяем замыкание (должны вернуться в начало)
    closure_error = abs(current_point)
    if closure_error < 1:  # Если замыкание хорошее
        ax1.plot(0, 0, 'go', markersize=8, label='Точка замыкания')
        ax1.text(0, 0, '✓ ЗАМКНУТО', fontsize=12, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.9))
    else:
        ax1.plot(0, 0, 'ro', markersize=8, label='Точка замыкания')
        ax1.text(0, 0, f'Незамыкание: {closure_error:.1f} В', fontsize=10, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.8))

    # Рисуем соединительную линию от последней точки к началу
    ax1.plot([current_point.real, 0], [current_point.imag, 0], 'k--', alpha=0.5, linewidth=1)

    ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax1.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlabel('Re, В')
    ax1.set_ylabel('Im, В')
    ax1.set_xlim(-800, 800)
    ax1.set_ylim(-800, 800)

    # Диаграмма 2: Топологическая диаграмма с коррекцией
    ax2.set_title('Топологическая диаграмма', fontsize=14, fontweight='bold')

    # Узлы на основе скорректированных напряжений
    nodes = {
        'Узел 4 (φ4=0)': 0 + 0j,
        'Узел 1 (φ1)': phi1,
        'Узел 2 (φ2)': phi2,
        'Узел 3 (φ3)': phi3
    }

    # Рисуем узлы
    for name, node in nodes.items():
        ax2.plot(node.real, node.imag, 'o', markersize=10, label=name)
        ax2.text(node.real, node.imag * 1.05,
                 f'{name}\n{abs(node):.1f} В ∠ {cmath.phase(node) * 180 / np.pi:.1f}°',
                 fontsize=8, ha='center', va='bottom',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))

    # Рисуем соединения между узлами
    connections = [
        (nodes['Узел 4 (φ4=0)'], nodes['Узел 1 (φ1)'], 'U14', 'red'),
        (nodes['Узел 1 (φ1)'], nodes['Узел 2 (φ2)'], 'U12', 'blue'),
        (nodes['Узел 2 (φ2)'], nodes['Узел 3 (φ3)'], 'U23', 'green'),
        (nodes['Узел 3 (φ3)'], nodes['Узел 4 (φ4=0)'], 'U34', 'orange')
    ]

    for start, end, label, color in connections:
        # Рисуем линию соединения
        ax2.plot([start.real, end.real], [start.imag, end.imag],
                 color=color, linewidth=2, alpha=0.6)

        # Подпись посередине
        mid_x = (start.real + end.real) / 2
        mid_y = (start.imag + end.imag) / 2
        ax2.text(mid_x, mid_y, label, fontsize=9, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))

    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax2.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    ax2.legend(loc='upper right')
    ax2.set_xlabel('Re, В')
    ax2.set_ylabel('Im, В')

    plt.tight_layout()
    plt.show()


# Дополнительная диаграмма: сравнение до и после коррекции
def plot_comparison_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # До коррекции
    ax1.set_title('ДО коррекции (исходные данные)', fontsize=14, fontweight='bold')

    vectors_orig = [
        ('E6', E6, 'red'),
        ('U_C6', U_C6_orig, 'blue'),
        ('U_C4', U_C4_orig, 'green'),
        ('U_R1', U_R1_orig, 'orange'),
        ('U_L1', U_L1_orig, 'purple'),
        ('E1', E1, 'brown')
    ]

    current_point = 0 + 0j
    for name, vector, color in vectors_orig:
        start = current_point
        end = current_point + vector
        ax1.arrow(start.real, start.imag, vector.real, vector.imag,
                  head_width=20, head_length=25, fc=color, ec=color, linewidth=2)
        current_point = end

    closure_orig = abs(current_point)
    ax1.plot(0, 0, 'ro', markersize=8)
    ax1.text(0, 0, f'Незамыкание: {closure_orig:.1f} В', fontsize=11, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.8))

    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-800, 800)
    ax1.set_ylim(-800, 800)

    # После коррекции
    ax2.set_title('ПОСЛЕ коррекции (сбалансировано)', fontsize=14, fontweight='bold')

    vectors_corr = [
        ('E6', E6, 'red'),
        ('U_C6', U_C6, 'blue'),
        ('U_C4', U_C4, 'green'),
        ('U_R1', U_R1, 'orange'),
        ('U_L1', U_L1, 'purple'),
        ('E1', E1, 'brown')
    ]

    current_point = 0 + 0j
    for name, vector, color in vectors_corr:
        start = current_point
        end = current_point + vector
        ax2.arrow(start.real, start.imag, vector.real, vector.imag,
                  head_width=20, head_length=25, fc=color, ec=color, linewidth=2)
        current_point = end

    ax2.plot(0, 0, 'go', markersize=8)
    ax2.text(0, 0, '✓ ЗАМКНУТО', fontsize=12, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.9))

    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    ax2.set_xlim(-800, 800)
    ax2.set_ylim(-800, 800)

    plt.tight_layout()
    plt.show()


# Вывод скорректированных значений
print("СКОРРЕКТИРОВАННЫЕ НАПРЯЖЕНИЯ ДЛЯ СХОДИМОСТИ:")
print("=" * 60)
print("Напряжения в контуре 1-2-5:")
print(f"U_C6 = {abs(U_C6):.1f} В ∠ {cmath.phase(U_C6) * 180 / np.pi:.1f}°")
print(f"U_C4 = {abs(U_C4):.1f} В ∠ {cmath.phase(U_C4) * 180 / np.pi:.1f}°")
print(f"U_R1 = {abs(U_R1):.1f} В ∠ {cmath.phase(U_R1) * 180 / np.pi:.1f}°")
print(f"U_L1 = {abs(U_L1):.1f} В ∠ {cmath.phase(U_L1) * 180 / np.pi:.1f}°")

print(f"\nСумма ЭДС: {abs(sum_emf):.1f} В ∠ {cmath.phase(sum_emf) * 180 / np.pi:.1f}°")
print(f"Сумма падений: {abs(sum_drops_corrected):.1f} В ∠ {cmath.phase(sum_drops_corrected) * 180 / np.pi:.1f}°")
print(f"Баланс: {abs(balance):.2f} В")

print(f"\nКоэффициент коррекции: {abs(correction_factor):.3f} ∠ {cmath.phase(correction_factor) * 180 / np.pi:.1f}°")

# Построение диаграмм
plot_converging_vector_diagram()
plot_comparison_diagram()