# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint

num_list = [randint(0, 10) for i in range(int(input("Количество элементов? ")))]
print(num_list)
print(f"Сумма элементов на нечетной позиции: {sum(num_list[1::2])}")