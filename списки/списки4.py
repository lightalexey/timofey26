a = [12, 43, -32, 0, 340, 3, 32]
# maximum = -100000
maximum = a[0]
for i in a:
    if i > maximum:
        maximum = i
print(maximum)

maximum = a[0]
for i in range(len(a)):
    if a[i] > maximum:
        maximum = a[i]
print(maximum)

minimum = a[0]
for i in a:
    if i < minimum:
        minimum = i
print(minimum)
print(max(a), min(a))