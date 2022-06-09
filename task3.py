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
# Пример: при d = 0.001,  c= 3.141.                - не осилил!!! Даже после раззбора, не понял как применить Ряд Лейбница!!!


# 3.	Составить список простых множителей натурального числа N

'''
def divising(number):
    divisor = 2
    list_of_divisors = []
    while number >= divisor:
        if number % divisor == 0:
            list_of_divisors.append(divisor)
            number//=divisor
        else:
            divisor+=1           
    return list_of_divisors


number = int(input('Enter natural number: '))
print(divising(number))
'''

# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
'''
def selection_unique_numbers(number_list):
    total_list = set(number_list)
    return total_list


number_list = [1, 2, 3, 5, 1, 5, 3, 10]
total = list(selection_unique_numbers(number_list))
print(total)
'''
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
'''
import random


def make_file_with_numbers(count_of_number):
    with open('file_number_list.txt', 'w') as data:
        for i in range(count_of_number):
            data.write(str(random.randint(-100, 100))+' ')


def get_row(str_from_file):
    with open('file_number_list.txt', 'r') as data:
        for i in data:
            str_from_file += i
    return str_from_file


def delete_even_numbers(total_list):
    in_between_list = []
    for i in total_list:
        if int(i) % 2 != 0:
            in_between_list.append(int(i))
    return in_between_list


def rewrite_in_new_file(total_list):
    with open('totalfile.txt', 'w') as data:
        data.write(str(total_list))


count_of_numbers = int(input('Enter tht count of number: '))
make_file_with_numbers(count_of_numbers)
str_from_file = ''
str_from_file = get_row(str_from_file)
# print(str_from_file)
total_list = str_from_file.split()
# print(total_list)
total_list = delete_even_numbers(total_list)
print(total_list)
rewrite_in_new_file(total_list)
'''
