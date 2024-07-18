# Figure lib

## Описание

Эта библиотека предоставляет возможности для вычисления площадей фигур

## Установка

Для установки библиотеки скопируйте файлы `figures.py` и `test_geometry.py` в ваш проект.

## Использование

### Класс `Figure`

Абстрактный базовый класс для всех фигур.


### Класс `Triangle`

Класс для представления треугольника.

#### Атрибуты

- `a (float)`: Длина первой стороны треугольника.
- `b (float)`: Длина второй стороны треугольника.
- `c (float)`: Длина третьей стороны треугольника.

#### Методы

- `__init__(self, a: float, b: float, c: float)`: Инициализирует треугольник с заданными сторонами.
- `area(self) -> float`: Вычисляет площадь треугольника по формуле Герона.
- `is_right_triangle(self) -> bool`: Проверяет, является ли треугольник прямоугольным.

#### Пример использования

```python
from figures import Triangle

triangle = Triangle(6, 8, 10)
print(f"Area of the triangle: {triangle.area()}")
print(f"Is the triangle right-angled? {'Yes' if triangle.is_right_triangle() else 'No'}")
```

### Класс `Circle`

Класс представляет круг с заданным радиусом.

#### Атрибуты

- `r (float)`: Радиус круга.

#### Методы

- `__init__(self, r: float)`: Инициализирует круг с заданным радиусом.
- `area(self) -> float`: Вычисляет площадь круга по формуле \( \pi r^2 \).

#### Пример использования

```python
from figures import Circle

# Создание круга с радиусом 7
circle = Circle(7)

# Вычисление и вывод площади круга
print(f"Area of the circle: {circle.area()}")
```