for a in range(10_000_000, 100_000_000 + 10000):  # 10**10..
    k = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            k = False
            break
    if k:
        print(a)
