def famous_quote(autor_name, text):
    result = autor_name + text
    return result


print(famous_quote('Sherlock Holmes', ' once said, "You know my methods, Watson."'))


def number_eight():
    print(4 + 4)
    print(10 - 2)
    print(4 * 2)
    print(64 // 8)
    print(2**3)


number_eight()


def name_age():
    name = input("Type in your name: ")
    age = int(input("Type in your age: "))
    print("Hello " + name +". You are " + str(age) + " years old.")
    print("Hello {}. You are {} years old.".format(name, age))
    print(f"Hello {name}. You are {age} years old.")


name_age()


def swap_integers():
    x = int(input("x = "))
    y = int(input("y = "))
    print("x = " + str(x))
    print("y = " + str(y))
    z = x
    x = y
    y = z
    print("x = " + str(x))
    print("y = " + str(y))


swap_integers()


def check_numbers(number1, number2):
    print("Number 1 is : " + str(number1))
    print("Number 2 is : " + str(number2))
    if (number1 % 6 == 0) or (number2 % 6 == 0):
        print("One Number is divisible by 6.")
    if (number1 % 10 != 0) or (number2 % 10 != 0):
        print("Both numbers are not divisible by 10.")
    if ((number1 % 6 == 0) or (number2 % 6 == 0)) and ((number1 % 10 != 0) or (number2 % 10 != 0)):
        return True
    else:
        return False

#variablen erstellen und diese beim aufruf der funktion verweden
print(check_numbers(int(input("1. Number:")), int(input("2. Number:"))))


def sum_up(number1, number2):
    if number2 < number1:
        print("The second number must be greater than the first.")
    else:
        result = 0
        for i in range(number1, number2 + 1):
            result += i
    print(number1, end=" + ")
    while number1 < number2:
        number1 += 1
        if number1 < number2:
            print(number1, end=" + ")
        if number1 == number2:
            print(number1, end="")

    print(" =", result)
    return result


sum_up(10,20)


def sequence(number):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    if number >= 0 and number < 10:
        numbers.remove(number)
    else:
        print("Error - this number is not between 0 - 9")
    for x in numbers:
        print(x,end=" ")


sequence(int(input("Type in a number between 0-9: ")))


def check_string(text):
    if text.startswith("A") or text.startswith("a") or text.endswith("a") or text.endswith("A"):
        return True
    else:
        return False


check_string(input("Type in a word: "))


def triangle(rows):
    start = 1
    while start <= rows:
        new_row = start + 1
        print("* " * start)
        start = new_row


triangle(int(input("Type in a number: ")))
#Warum muss man zwischen einer Funktion und dem Aufrufen einer Funktion 2 Zeilen Abstand lassen? Ich habe es ohne Abstand auch schon aufgerufen und es hat funktioniert. Ist es wegen der übersichtlicheren Lesbarkeit?