# ax^2+bx+c=0
a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Действительных решений нет")
if d > 0:
    х1 = (-b + d ** 0.5) / 2 / a
    x2 = (-b - d ** 0.5) / 2 / a
    print('x1=', х1, 'x2=', x2)
if d == 0:
    x1 = -b / (2 * a)
    print('x1=x2=', x1)
