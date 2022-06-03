# 1.	Найти НОК двух чисел
'''
import math

def Finding_GCD(num1, num2):                       #greatest common divisor(GCD) - наибольший общий делитель
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2
  

number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
gcd = Finding_GCD(number_1, number_2)
LСM = ((number_1*number_2)// gcd)                                      #Least common multiple (LCM) - наименьшее общее кратное 
print(f'Least common multiple numbers {number_1} and {number_2} = {LСM}')
'''




# 2.	Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
# 3.	Составить список простых множителей натурального числа N
# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
