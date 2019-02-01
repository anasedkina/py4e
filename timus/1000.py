import math


def quadratic_equation(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 'no real roots'
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return (x1, x2)


print(quadratic_equation(4, 0, 0))
