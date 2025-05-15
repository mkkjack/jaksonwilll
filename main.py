import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_conductor(length, height, upper_radius, lower_radius):
    """
    Функция для отрисовки проводника с заданными параметрами
    
    Параметры:
    length (float): Длина проводника
    height (float): Высота проводника
    upper_radius (float): Радиус кривизны верхнего закругления
    lower_radius (float): Радиус кривизны нижнего закругления
    """
    # Проверяем корректность расположения центров окружностей
    upper_center_y = height - upper_radius  # y-координата центра верхней дуги
    lower_center_y = lower_radius           # y-координата центра нижней дуги
    
    if lower_center_y >= upper_center_y:
        raise ValueError("Параметры заданы неверно: центр нижней окружности выше или равен центру верхней окружности")
    
    # Создаем новый график
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Определяем цвета для каждого элемента
    colors = {
        'left_line': '#FF0000',      # Красный
        'top_line': '#00FF00',       # Зеленый
        'bottom_line': '#0000FF',    # Синий
        'right_line': '#FF00FF',     # Пурпурный
        'upper_arc': '#FFA500',      # Оранжевый
        'lower_arc': '#800080'       # Фиолетовый
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
    
    # Отрисовка правой вертикальной линии (соединяющей дуги)
    plt.plot([length, length], 
             [height-upper_radius, lower_radius], 
             color=colors['right_line'], 
             linewidth=2, 
             label='Правая сторона')
    
    # Добавляем верхнее закругление (дугу)
    upper_arc = Arc((length-upper_radius, height-upper_radius),
                   2*upper_radius, 2*upper_radius,
                   theta1=0, theta2=90,
                   color=colors['upper_arc'], 
                   linewidth=2,
                   label='Верхняя дуга')
    ax.add_patch(upper_arc)
    
    # Добавляем нижнее закругление (дугу)
    lower_arc = Arc((length-lower_radius, lower_radius),
                   2*lower_radius, 2*lower_radius,
                   theta1=270, theta2=360,
                   color=colors['lower_arc'], 
                   linewidth=2,
                   label='Нижняя дуга')
    ax.add_patch(lower_arc)
    
    # Настройка графика
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')  # Обеспечивает одинаковый масштаб по осям
    
    # Добавляем подписи осей
    plt.xlabel('Длина (мм)')
    plt.ylabel('Высота (мм)')
    plt.title('Схема проводника')
    
    # Устанавливаем пределы осей с небольшим отступом
    margin = max(upper_radius, lower_radius) * 0.2
    plt.xlim(-margin, length + margin)
    plt.ylim(-margin, height + margin)
    
    # Настраиваем легенду
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Увеличиваем размер фигуры, чтобы легенда не обрезалась
    plt.tight_layout()
    plt.show()

# Пример использования функции с тестовыми значениями
length = 100  # длина проводника
height = 20   # высота проводника
upper_radius = 20  # радиус верхнего закругления
lower_radius = 15  # радиус нижнего закругления

# Вызов функции для отрисовки проводника
try:
    draw_conductor(length, height, upper_radius, lower_radius)
except ValueError as e:
    print(f"Ошибка: {e}")

 