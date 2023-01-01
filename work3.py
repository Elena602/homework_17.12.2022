# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input("Введите число : "))
a = 0
summ = 0
for i in range (1, n + 1):
    a += (1 + 1 / i)**i 
    print(f'{i} : {round(a)}', end=" ")
    summ += a
print()
print(f"Полученная сумма последовательности (1+1/n)**n равна {round(summ, 2)}")