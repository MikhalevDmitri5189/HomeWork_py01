# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = input ('Ведите трехзначное число: ')
num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])
print('Сумма трёхзначного числа равняется:',num1 + num2 + num3)