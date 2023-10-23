def binary_search_guess_user_number():
    print("Загадайте число от 1 до 100. Я попробую угадать его.")
    min_num = 1
    max_num = 100
    attempts = 0

    while True:
        guess = (min_num + max_num) // 2
        print(f"Моя попытка: {guess}")
        attempts += 1

        user_feedback = input("Введите '+', '-', или '=', чтобы указать, больше, меньше или равно вашему числу: ")

        if user_feedback == "=":
            print(f"Ура! Я угадал число {guess} за {attempts} попыток.")
            break
        elif user_feedback == "+":
            min_num = guess + 1
        elif user_feedback == "-":
            max_num = guess - 1
        else:
            print("Пожалуйста, введите только '+', '-', или '='.")

# Запускаем игру
binary_search_guess_user_number()
