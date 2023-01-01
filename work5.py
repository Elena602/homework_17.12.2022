# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

# import random
# print("Enter number")
# n = int(input())
# list1 = [random.randint(-n,n) for i in range(n)]
# print(list1)
# print(random.sample(list1,n))

import random
#                    интервал для чисел               кол-во чисел
lst = [random.randint(0, 10) for i in range(random.randint(5, 20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")
