import time

first_question = input("Hello and welcome to the Calculator write the sign (*, /, +, - ONLY):   ")

error1 = "Not correct! you cannot take a number / 0"

if first_question == "*":
    number_one = int(input("Write the first number. ➡  "))
    number_two = int(input("Write the Second number. ➡  "))
    answer = number_one * number_two
    print(answer)


if first_question == "/":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    if number_two != 0:
        answer = number_one / number_two
        print(answer)
    else:
        print(error1)

if first_question == "+":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    answer = number_one + number_two
    print(answer)

if first_question == "-":
    number_one = int(input("Write the first number. ➡ "))
    number_two = int(input("Write the Second number. ➡ "))
    answer = number_one - number_two
    print(answer)
