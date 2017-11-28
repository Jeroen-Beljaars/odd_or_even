"""
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: 
one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

"""
Created by Jeroen at 28-11-2017
"""

# Ask the user for numbers
number = int(input("Choose a number "))
num = int(input("Give a number to devide the previous number by "))

# Run the functions and print the result
print(odd_or_even(number))
print(divide(number, num))


"""
Check if a number is:
Odd, Even or a multiple of 4

Return A string which tells the user what the outcome is
"""
def odd_or_even(number):
    if number % 4 == 0:
        return "The number is a multiple of 4"
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

"""
Check if number is devideble by num

Return if it is or isn't 
"""
def divide(number, num):
    if number % num == 0:
        return "{} devides evenly into {}".format(number, num)
    else:
        return "{} doesn't devide evenly into {}".format(number, num)