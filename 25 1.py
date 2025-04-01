for a in range (210235, 210300):
    k = 0
    for i in range (2, a//2 + 1):
        if a % i == 0:
            k += 1
    if k == 4:
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                print(i, end=' ')
        print()
