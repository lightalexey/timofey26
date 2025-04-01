k = 0
for i in range(100, 999 + 1):
    i1 = i // 100
    i2 = i // 10 % 10
    i3 = i % 10
    summ = i1 + i2 + i3
    if summ == 6:
        print(i, end=' ')
        k += 1  # k = k + 1 k++

print()
print('-----------------------')
print('количество равно', k)