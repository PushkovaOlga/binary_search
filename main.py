#напишите программу для бинарного поиска загаданного числа

def binary_search():
    min_num = int(input("Введите минимальное число"))
    max_num = int(input("Введите максимальное число"))
    center = (min_num + max_num) // 2

    while True:
        print(f"Ваше число {center}?")
        check = input("Если больше >, если меньше <, если равно =")

        if check == ">":
           min_num = center
           center = (min_num + max_num) // 2
        elif check == "<":
           max_num = center
           center = (min_num + max_num) // 2
        elif check == "=":
            print(f"Вы загадали {check}")
            break
        else:
            print("Я не знаю этого числа")


binary_search()