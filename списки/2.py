a = [12, 43, -32, 0, 0, 3, 32]
# Найти среднее арифметическое всех элементов
# Найти произведение ненулевых элементов
# Найти сумму положительных элементов
# Найти среднее арифметическое положительных элементов
summa = 0
for i in a:
    summa += i
summa = summa/len(a)
print(summa)
print(sum(a)/len(a))
proizv = 1
for i in a:
    if i != 0:
        proizv *= i
print(proizv)
summ = 0
k = 0
for i in a:
    if i>0:
        summ +=i
        k += 1
sred = summ / k     # summ /= k
print(sred)

