# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# n = int(input("n = "))
# m = 1
# multiplication = 1
# list = []
# while m <= n:
#     multiplication = multiplication * m
#     m = m + 1
#     for multiplication in list:
#         print(list)
# print(f'Произведение: {list}')

num = int(input("Введите число : "))
a = 1
for i in range(1, num + 1):
    a *= i
    print(a, end=" ")
print()
