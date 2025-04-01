a = input('введи все элементы через пробел:').split()
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [int(i) for i in input('введи все элементы через пробел:').split()]