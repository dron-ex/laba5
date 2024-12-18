def calculate_product_and_sum(numbers):
    # 1. Произведение элементов списка с четными номерами
    product_even_indices = 1
    for i in range(0, len(numbers), 2):  # проходим по четным индексам
        product_even_indices *= numbers[i]

    # 2. Сумма элементов между первым и последним нулями
    try:
        first_zero_index = numbers.index(0)
        last_zero_index = len(numbers) - 1 - numbers[::-1].index(0)

        if first_zero_index < last_zero_index:
            sum_between_zeros = sum(numbers[first_zero_index + 1:last_zero_index])
        else:
            sum_between_zeros = 0
    except ValueError:
        # Если нулей нет, возвращаем 0
        sum_between_zeros = 0

    return product_even_indices, sum_between_zeros


# Ввод данных пользователем
input_numbers = input("Введите целые числа, разделенные пробелами: ")
numbers = list(map(int, input_numbers.split()))

# Вычисление результатов
product, sum_between = calculate_product_and_sum(numbers)

# Вывод результатов
print("Произведение элементов с четными индексами:", product)
print("Сумма элементов между первым и последним нулями:", sum_between)

