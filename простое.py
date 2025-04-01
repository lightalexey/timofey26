a = 13
k = 0
for i in range(1, a + 1):
    if a % i == 0:
        k += 1
if k == 0:
    print("YES")
else:
    print("NO")



