# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint 

num_list = [randint(2, 10) for i in range(int(input("Количество элементов? ")))]
print(num_list)
print(
    [
        num_list[i] * num_list[-(i + 1)]
        for i in range(len(num_list) // 2 + len(num_list) % 2)
    ]
)