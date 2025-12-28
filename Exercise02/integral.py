import numpy as np
import scipy.integrate as spi

# Визначення функції та меж
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
y_max = f(b)  # Максимальне значення функції на відрізку [0, 2]

# Метод Монте-Карло
def monte_carlo_integral(n_points=100000):
    # Генеруємо випадкові точки у прямокутнику [a, b] x [0, y_max]
    x_random = np.random.uniform(a, b, n_points)
    y_random = np.random.uniform(0, y_max, n_points)
    
    # Визначаємо, скільки точок потрапило під криву
    points_under_curve = np.sum(y_random < f(x_random))
    
    # Площа прямокутника
    rectangle_area = (b - a) * y_max
    
    # Площа під кривою (наближена)
    integral_mc = rectangle_area * (points_under_curve / n_points)
    return integral_mc

# Перевірка за допомогою SciPy quad (Аналітичне наближення)
quad_result, error = spi.quad(f, a, b)

# Аналітичне значення (інтеграл x^2 = x^3/3)
analytical_value = (b**3 / 3) - (a**3 / 3)

# Виконання обчислень
n = 500000  # Кількість точок для Монте-Карло
mc_result = monte_carlo_integral(n)

print(f"Кількість точок: {n}")
print(f"Результат Монте-Карло: {mc_result:.6f}")
print(f"Результат SciPy quad:  {quad_result:.6f}")
print(f"Аналітичне значення:   {analytical_value:.6f}")
print(f"Абсолютна помилка MC:  {abs(mc_result - quad_result):.6f}")