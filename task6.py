# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

from random import randint

num_list = [randint(0, 10) for i in range(int(input("Количество элементов? ")))]
print(num_list)
shift = int(input("Введите сдвиг: "))
shift = shift % len(num_list)
print(num_list[-shift:] + num_list[:-shift])