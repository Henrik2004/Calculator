import time




first_question = input("Hello and welcome to the Calculator write the sign (*, /, +, - ONLY) now:   ")


if first_question == "*":
    number_one = int(input("Write the first number. ➡  "))
    number_two = int(input("Write the Second number. ➡  "))
    answer = number_one * number_two
    print(number_one * number_two)


if first_question == "/":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    answer = number_one * number_two
    print(number_one * number_two)

if first_question == "+":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    answer = number_one * number_two
    print(number_one * number_two)

if first_question == "-":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    answer = number_one * number_two
    print(number_one * number_two)


error1 = "Not correct! you cannot take " + str(number_one) + " / 0"
if first_question == "/":
    if number_two == 0:
        print(error1)
