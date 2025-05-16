import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math

def find_circle_intersection(h, x1, y1, r1, x2, y2, r2):
    """
    Находит точки пересечения двух окружностей
    """
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"\n=== Расчет пересечения окружностей ===")
    print(f"Параметры окружности 1: центр=({x1}, {y1}), радиус={r1}")
    print(f"Параметры окружности 2: центр=({x2}, {y2}), радиус={r2}")
    print(f"Расстояние между центрами (d): {d}")
    if h > r1 + r2 or h < abs(r1 - r2):
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

def rotate_point(x, y, angle_degrees, origin=(0, 0)):
    """
    Поворачивает точку (x, y) вокруг точки origin на угол angle_degrees
    
    Args:
        x, y (float): Координаты точки
        angle_degrees (float): Угол поворота в градусах
        origin (tuple): Точка, вокруг которой происходит поворот
        
    Returns:
        tuple: Новые координаты точки (x_new, y_new)
    """
    # Преобразуем угол в радианы
    angle_rad = math.radians(angle_degrees)
    
    # Сдвигаем точку относительно центра вращения
    x_shifted = x - origin[0]
    y_shifted = y - origin[1]
    
    # Поворачиваем точку
    x_rotated = x_shifted * math.cos(angle_rad) - y_shifted * math.sin(angle_rad)
    y_rotated = x_shifted * math.sin(angle_rad) + y_shifted * math.cos(angle_rad)
    
    # Возвращаем точку обратно
    x_new = x_rotated + origin[0]
    y_new = y_rotated + origin[1]
    
    return x_new, y_new

def draw_conductor(length, height, upper_radius, lower_radius, rotation_angle=0):
    """
    Функция для отрисовки проводника с заданными параметрами и поворотом
    
    Args:
        length (float): Длина проводника
        height (float): Высота проводника
        upper_radius (float): Радиус верхнего закругления
        lower_radius (float): Радиус нижнего закругления
        rotation_angle (float): Угол поворота всей фигуры в градусах
    """
    print(f"\n=== Параметры проводника ===")
    print(f"Длина: {length}")
    print(f"Высота: {height}")
    print(f"Верхний радиус: {upper_radius}")
    print(f"Нижний радиус: {lower_radius}")
    print(f"Угол поворота: {rotation_angle}")
    
    # Определяем центр вращения (центр фигуры)
    rotation_center = (length/2, height/2)
    
    # Собираем все важные точки до поворота
    points = {
        'left_bottom': (0, 0),
        'left_top': (0, height),
        'right_top': (length-upper_radius, height),
        'right_bottom': (length-lower_radius, 0),
        'upper_center': (length - upper_radius, height - upper_radius),
        'lower_center': (length - lower_radius, lower_radius)
    }
    
    # Поворачиваем все точки
    rotated_points = {
        key: rotate_point(x, y, rotation_angle, rotation_center)
        for key, (x, y) in points.items()
    }
    
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
    
    # Проверяем пересечение окружностей
    intersections = find_circle_intersection(height,
        points['upper_center'][0], points['upper_center'][1], upper_radius,
        points['lower_center'][0], points['lower_center'][1], lower_radius
    )
    
    # Отрисовка основных линий с учетом поворота
    plt.plot([rotated_points['left_bottom'][0], rotated_points['left_top'][0]],
             [rotated_points['left_bottom'][1], rotated_points['left_top'][1]],
             color=colors['left_line'], linewidth=2, label='Левая сторона')
             
    plt.plot([rotated_points['left_top'][0], rotated_points['right_top'][0]],
             [rotated_points['left_top'][1], rotated_points['right_top'][1]],
             color=colors['top_line'], linewidth=2, label='Верхняя сторона')
             
    plt.plot([rotated_points['left_bottom'][0], rotated_points['right_bottom'][0]],
             [rotated_points['left_bottom'][1], rotated_points['right_bottom'][1]],
             color=colors['bottom_line'], linewidth=2, label='Нижняя сторона')
    
    if not intersections:
        # Если окружности не пересекаются
        right_top = rotate_point(length, height-upper_radius, rotation_angle, rotation_center)
        right_bottom = rotate_point(length, lower_radius, rotation_angle, rotation_center)
        
        plt.plot([right_top[0], right_bottom[0]], 
                 [right_top[1], right_bottom[1]],
                 color=colors['right_line'], linewidth=2, label='Правая сторона')
                 
        # Добавляем дуги с учетом поворота
        upper_arc = Arc(rotated_points['upper_center'],
                       2*upper_radius, 2*upper_radius,
                       theta1=rotation_angle, theta2=rotation_angle+90,
                       color=colors['upper_arc'], linewidth=2,
                       label='Верхняя дуга')
        ax.add_patch(upper_arc)
        
        lower_arc = Arc(rotated_points['lower_center'],
                       2*lower_radius, 2*lower_radius,
                       theta1=rotation_angle+270, theta2=rotation_angle+360,
                       color=colors['lower_arc'], linewidth=2,
                       label='Нижняя дуга')
        ax.add_patch(lower_arc)
    else:
        intersection = None
        for point in intersections:
            if point[0] >= points['upper_center'][0]:
                intersection = point
                break
                
        if intersection:
            # Поворачиваем точку пересечения
            rotated_intersection = rotate_point(intersection[0], intersection[1], 
                                             rotation_angle, rotation_center)
            
            # Вычисляем углы для дуг с учетом поворота
            upper_angle = math.degrees(calculate_angle(points['upper_center'][0], 
                                                     points['upper_center'][1], 
                                                     intersection[0], 
                                                     intersection[1]))
            lower_angle = math.degrees(calculate_angle(points['lower_center'][0], 
                                                     points['lower_center'][1], 
                                                     intersection[0], 
                                                     intersection[1]))
            
            # Добавляем дуги с учетом поворота
            upper_arc = Arc(rotated_points['upper_center'],
                          2*upper_radius, 2*upper_radius,
                          theta1=upper_angle+rotation_angle, 
                          theta2=90+rotation_angle,
                          color=colors['upper_arc'], linewidth=2,
                          label='Верхняя дуга')
            ax.add_patch(upper_arc)
            
            lower_arc = Arc(rotated_points['lower_center'],
                          2*lower_radius, 2*lower_radius,
                          theta1=270+rotation_angle, 
                          theta2=lower_angle+rotation_angle,
                          color=colors['lower_arc'], linewidth=2,
                          label='Нижняя дуга')
            ax.add_patch(lower_arc)
    
    # Настройка графика
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    
    plt.xlabel('X (мм)')
    plt.ylabel('Y (мм)')
    plt.title(f'Схема проводника (поворот {rotation_angle}°)')
    
    # Расширяем границы графика для учета поворота
    margin = max(length, height) * 0.2
    plt.xlim(min(p[0] for p in rotated_points.values()) - margin,
             max(p[0] for p in rotated_points.values()) + margin)
    plt.ylim(min(p[1] for p in rotated_points.values()) - margin,
             max(p[1] for p in rotated_points.values()) + margin)
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Пример использования функции с тестовыми значениями
length = 100  # длина проводника
height = 40   # высота проводника
upper_radius = 20  # радиус верхнего закругления
lower_radius = 10  # радиус нижнего закругления
angle1 = 35  # угол поворота в градусах

# Вызов функции для отрисовки проводника с поворотом
try:
    draw_conductor(length, height, upper_radius, lower_radius, angle1)
except ValueError as e:
    print(f"Ошибка: {e}")