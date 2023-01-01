# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input("n = "))
k = abs(n)
sum = 0
while (k % 10) > 0:
    k = k * 10
while (k > 0): 
    sum = sum + (k % 10)
    k = k // 10
print(f'Сумма цифр: {sum}')

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)


# num = str(abs(float(input("Введите число: ")))).replace(".", "")

# result = 0
# for i in num:
#     result += int(i)

# print(result)
