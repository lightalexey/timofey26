a = int(input())
b = int(input())
c = int(input())
if a < b + c:
    if b < a + c:
        if c < a + b:
            # print("YES")
            if a == b == c:
                print("Равносторонний")
            else:
                if a == b or b ==c or a ==c:
                    print("Равнобедренный")
                else:
                    if c ** 2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2:
                        print("Прямоугольный")
                    else:
                        print("Произвольный")
        else:
            print("NO")
