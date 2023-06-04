def f(x, y):
    # Задайте функцию, которую нужно интегрировать
    return 1 * x

def double_integral(a, b, c, d, n, m):
    # a, b, c - границы интегрирования по x
    # d - функция, определяющая правую границу по y в зависимости от x
    # n, m - количество прямоугольников по x и y соответственно

    dx = (b - a) / n  # Шаг по x

    integral_sum = 0

    for i in range(n):
        x = a + i * dx  # Левая граница прямоугольника по x
        dy = (d(x) - c) / m  # Шаг по y для данного x

        for j in range(m):
            y = c + j * dy  # Левая граница прямоугольника по y

            # Вычисляем значение функции в центре прямоугольника
            xi = x + dx / 2
            yj = y + dy / 2
            f_value = f(xi, yj)

            integral_sum += f_value * dx * dy

    return abs(integral_sum)

# Пример вычисления двойного интеграла
a = 2
b = 0
c = 0
d = lambda x: -x**2 + 2*x + 1  # Граница d зависит от x
n = 100
m = 100

result = double_integral(a, b, c, d, n, m)
print(result)
