# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списка на основе n, а позиции элементов lst2=[3,1].

import random
n = int(input("Введите целое положительное число : "))
List = []
listOfMultiplication = []
if n > 0:
    for i in range (n):
        List.append(random.randint(-1 * n, n))
    for i in range(2):
        listOfMultiplication.append(random.randint(0, n - 1))
    print(f'Сформированный список {List}.')
    print(f'Список с индексами {listOfMultiplication}.')
    print(f'Произведение цифр: {List[listOfMultiplication[0]]} * {List[listOfMultiplication[1]]} = {List[listOfMultiplication[0]]} * {List[listOfMultiplication[1]]}.')
else:
    print(f'Введенное число {n} является отрицательным.')