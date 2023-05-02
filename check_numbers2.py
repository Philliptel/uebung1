def check_numbers(number1, number2):
    print("Number 1 = " + str(number1))
    print("Number 2 = " + str(number2))
    if (number1 % 6 == 0) or (number2 % 6 == 0):
            print("One number is divisible by 6")
    if (number1 % 10 != 0) or (number2 % 10 != 0):
            print("Both numbers are not divisible by 10")
check_numbers(5,10)