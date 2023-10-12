def triangle(n):
    if n % 2 == 0:
        print("Пожалуйста, введите нечетное натуральное число.")
    else:
        for i in range(1, n // 2 + 2):
            print("*" * i)
        for i in range(n // 2, 0, -1):
            print("*" * i)
