a = []
#print(a)
#a = [12, 21, 2, 0]
#print(a)
#print(*a)
n = int(input('введи количество элементов:'))
for i in range(n):
    number = input('Введи элемент:')
    a.append(number)
print(*a)