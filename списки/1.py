a = [12, 43, -32, 0, 0, 3, 32]
l = len(a)
print('Количество элементов списка равно', l)
print(a[0], a[l-1], a[-1])
summa = 0
for i in range(l):
    summa += a[i]
print('Сумма элементов равна', summa)
summa = 0
for i in a:
    summa += i
print('Сумма элементов равна', summa)
print(sum(a))
print('Исходные данные:')
for i in range(l):
    print(a[i], end=' ')
print()
for i in a:
    print(i, end=' ')
print()
print(a)
print(*a)