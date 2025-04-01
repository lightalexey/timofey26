for a in range (312614,312651+1):
    k = 0
    for i in range (1,a+1):
        if a % i == 0:
            k += 1
    if k == 6:
        for i in range(1,a + 1):
            if a % i == 0:
                print(i, end=' ')
        print()
