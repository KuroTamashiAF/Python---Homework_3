def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


number1 = int(input("ENTER numb1: "))
number2 = int(input("ENTER numb2: "))
a = gcd_rem_division(number1,number2)
print(a)

    
