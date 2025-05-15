import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math

def find_circle_intersection( x1, y1, r1, x2, y2, r2):
    """
    Находит точки пересечения двух окружностей
    """
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"\n=== Расчет пересечения окружностей ===")
    print(f"Параметры окружности 1: центр=({x1}, {y1}), радиус={r1}")
    print(f"Параметры окружности 2: центр=({x2}, {y2}), радиус={r2}")
    print(f"Расстояние между центрами (d): {d}")
    if y1>y2:
        print(f"Окружности не пересекаются:")
        print(f"- Сумма радиусов: {r1 + r2}")
        print(f"- Разность радиусов: {abs(r1 - r2)}")
        return None  # Окружности не пересекаются
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    
    print(f"Промежуточные расчеты:")
    print(f"- a = {a}")
    print(f"- h = {h}")
    
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d
    
    x4 = x3 + h * (y2 - y1) / d
    y4 = y3 - h * (x2 - x1) / d
    
    x5 = x3 - h * (y2 - y1) / d
    y5 = y3 + h * (x2 - x1) / d
    
    print(f"Найденные точки пересечения:")
    print(f"- Точка 1: ({x4:.2f}, {y4:.2f})")
    print(f"- Точка 2: ({x5:.2f}, {y5:.2f})")
    
    return [(x4, y4), (x5, y5)]

def calculate_angle(x_center, y_center, x_point, y_point):
    """
    Вычисляет угол между центром окружности и точкой в радианах
    """
    angle = math.atan2(y_point - y_center, x_point - x_center)
    print(f"\nРасчет угла:")
    print(f"- Центр: ({x_center}, {y_center})")
    print(f"- Точка: ({x_point:.2f}, {y_point:.2f})")
    print(f"- Угол в радианах: {angle:.4f}")
    print(f"- Угол в градусах: {math.degrees(angle):.2f}")
    return angle

def draw_conductor(length, height, upper_radius, lower_radius):
    """
    Функция для отрисовки проводника с заданными параметрами
    
    Args:
        length (float): Длина проводника
        height (float): Высота проводника
        upper_radius (float): Радиус верхнего закругления
        lower_radius (float): Радиус нижнего закругления
    """
    print(f"\n=== Параметры проводника ===")
    print(f"Длина: {length}")
    print(f"Высота: {height}")
    print(f"Верхний радиус: {upper_radius}")
    print(f"Нижний радиус: {lower_radius}")
    
    # Проверяем корректность расположения центров окружностей
    upper_center_x = length - upper_radius
    upper_center_y = height - upper_radius
    lower_center_x = length - lower_radius
    lower_center_y = lower_radius
    
    print(f"\nКоординаты центров окружностей:")
    print(f"Верхняя окружность: ({upper_center_x}, {upper_center_y})")
    print(f"Нижняя окружность: ({lower_center_x}, {lower_center_y})")

    # Проверяем пересечение окружностей
    intersections = find_circle_intersection(
        upper_center_x, upper_center_y, upper_radius,
        lower_center_x, lower_center_y, lower_radius
    )
    
    print(f"\nРезультат поиска пересечений:")
    print(f"Найдены пересечения: {intersections is not None}")
    if intersections:
        print(f"Количество точек пересечения: {len(intersections)}")
        for i, point in enumerate(intersections, 1):
            print(f"Точка {i}: ({point[0]:.2f}, {point[1]:.2f})")

    # Создаем новый график
    fig, ax = plt.subplots(figsize=(10, 6))

    # Определяем цвета для каждого элемента
    colors = {
        'left_line': '#FF0000',
        'top_line': '#00FF00',
        'bottom_line': '#0000FF',
        'right_line': '#FF00FF',
        'upper_arc': '#FFA500',
        'lower_arc': '#800080'
    }

    # Отрисовка левой вертикальной линии
    plt.plot([0, 0], [0, height], 
             color=colors['left_line'], 
             linewidth=2, 
             label='Левая сторона')

    # Отрисовка горизонтальных линий
    plt.plot([0, length-upper_radius], [height, height], 
             color=colors['top_line'], 
             linewidth=2, 
             label='Верхняя сторона')

    plt.plot([0, length-lower_radius], [0, 0], 
             color=colors['bottom_line'], 
             linewidth=2, 
             label='Нижняя сторона')

    if not intersections:
        print("\nОкружности не пересекаются - рисуем прямую линию")
        # Если окружности не пересекаются, соединяем их прямой линией
        plt.plot([length, length], 
                 [height-upper_radius, lower_radius], 
                 color=colors['right_line'], 
                 linewidth=2, 
                 label='Правая сторона')
        
        # Добавляем верхнее закругление (дугу)
        upper_arc = Arc((upper_center_x, upper_center_y),
                       2*upper_radius, 2*upper_radius,
                       theta1=0, theta2=90,
                       color=colors['upper_arc'], 
                       linewidth=2,
                       label='Верхняя дуга')
        ax.add_patch(upper_arc)

        # Добавляем нижнее закругление (дугу)
        lower_arc = Arc((lower_center_x, lower_center_y),
                       2*lower_radius, 2*lower_radius,
                       theta1=270, theta2=360,
                       color=colors['lower_arc'], 
                       linewidth=2,
                       label='Нижняя дуга')
        ax.add_patch(lower_arc)
    else:
        print("\nОбработка пересечений:")
        # Если есть пересечение, находим подходящую точку пересечения
        intersection = None
        for point in intersections:
            print(f"Проверка точки: ({point[0]:.2f}, {point[1]:.2f})")
            if point[0] >= upper_center_x:  # Точка в 1-й или 4-й четверти
                intersection = point
                print(f"Выбрана точка пересечения: ({point[0]:.2f}, {point[1]:.2f})")
                break
        
        if intersection:
            # Вычисляем углы для дуг
            upper_angle = math.degrees(calculate_angle(upper_center_x, upper_center_y, intersection[0], intersection[1]))
            lower_angle = math.degrees(calculate_angle(lower_center_x, lower_center_y, intersection[0], intersection[1]))
            
            print(f"\nРассчитанные углы:")
            print(f"Верхний угол: {upper_angle:.2f}°")
            print(f"Нижний угол: {lower_angle:.2f}°")
            
            # Добавляем верхнее закругление (дугу)
            upper_arc = Arc((upper_center_x, upper_center_y),
                           2*upper_radius, 2*upper_radius,
                           theta1=upper_angle, theta2=90,
                           color=colors['upper_arc'], 
                           linewidth=2,
                           label='Верхняя дуга')
            ax.add_patch(upper_arc)

            # Добавляем нижнее закругление (дугу)
            lower_arc = Arc((lower_center_x, lower_center_y),
                           2*lower_radius, 2*lower_radius,
                           theta1=270, theta2=lower_angle,
                           color=colors['lower_arc'], 
                           linewidth=2,
                           label='Нижняя дуга')
            ax.add_patch(lower_arc)

    # Настройка графика
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')

    plt.xlabel('Длина (мм)')
    plt.ylabel('Высота (мм)')
    plt.title('Схема проводника')

    margin = max(upper_radius, lower_radius) * 0.2
    plt.xlim(-margin, length + margin)
    plt.ylim(-margin, height + margin)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Пример использования функции с тестовыми значениями
length = 100  # длина проводника
height = 10   # высота проводника
upper_radius = 20  # радиус верхнего закругления
lower_radius = 30 # радиус нижнего закругления

# Вызов функции для отрисовки проводника
try:
    draw_conductor(length, height, upper_radius, lower_radius)
except ValueError as e:
    print(f"Ошибка: {e}")