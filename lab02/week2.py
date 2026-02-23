# TASK 1 done
# Declare a function that prompts the end-user to enter their name and then prints a greeting message in one of four different languages. The default language should be English

'''
def greet_user(language="English"):

    name = input("What is your name? ")

    if language =="English":
        greeting = "Hello"

    elif language =="Spanish":
        greeting = "Hola"
    elif language =="Polish":
        greeting = "Cześć"
    elif language =="Italian":
        greeting = "Ciao"   
    else:
        greeting = "Hello"

    print(f"{greeting}, {name}!")

greet_user()
'''

# TASK 2 done
#  Write a program (a function) that asks the user to enter their name and age in years. 
# The program should then calculate the number of months and days based on the given age and print the results, note that the Programme should consider leap years into account

'''
name = input("What is your name?")
age = int(input("What is your age (in years)?"))

# Calculate months 
age_months = int(age) * 12

# Calculate days
leapYears = int(age) // 4
age_days = int(age) * 365 + leapYears

print("You live ",age_months, "months")
print("You live ",age_days, "days") 
'''

#TASK 3 done
# Write a Python function that calculates the sum of all numbers from 1 to n using a for loop. Then, modify the function to use a while loop instead.
#  The function should return the calculated sum.

# if loop

'''
limit = int(input("Enter upper limit for a list: "))

numbers = list(range(1, limit + 1)) 
print("Generated list:", numbers)

total = 0
for num in numbers:
    total += num

print(total)
'''

# while loop

''' limit = int(input("Enter upper limit for a list: "))

numbers = list(range(1, limit + 1)) 
print("Generated list:", numbers)

total = 0
i = 0

while i < len(numbers):
    total +=numbers[i]
    i += 1

print(total) '''

# TASK 4 done
# Write a Python function named divisible that takes a lower_bound as input. The function should:
# (a) First check if the lower_bound is negative, if not exit the Programme.
# (b) Generate numbers starting from lower_bound up to its negative counterpart (inclusive), incrementing by 7.
# (c) For each number, check the following conditions: If the number is divisible by 5 AND negative, or If the number is divisible by 9, then print the number followed by "Yes".

'''
def divisible(lower_bound):
    # (a) Check if lower_bound is negative
    if lower_bound >= 0:
        return  # exit the function

    # (b) Generate numbers from lower_bound to its negative counterpart, incrementing by 7
    upper_bound = -lower_bound
    for num in range(lower_bound, upper_bound + 1, 7):
        # (c) Check the conditions
        if (num % 5 == 0 and num < 0) or (num % 9 == 0):
            print(num, "Yes")

# Example usage
divisible(-150)
'''

# TASK 5
# Write a Python function that takes a list of integers as input and performs the following operations:
# (a) Separate the numbers into two lists: Even numbers and Odd numbers.
# (b) Filter the even numbers to only include those divisible by 4.
# (c) Reverse the list of odd numbers.

'''
def process_numbers(numbers):
    # (a) Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # (b) Filter even numbers to only include those divisible by 4
    even_numbers = [num for num in even_numbers if num % 4 == 0]

    # (c) Reverse the list of odd numbers
    odd_numbers.reverse()

    return even_numbers, odd_numbers

# Take input from console
input_str = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]

# Call the function with the correct variable name
even_filtered, odd_reversed = process_numbers(numbers)

print("Even numbers divisible by 4:", even_filtered)
print("Reversed odd numbers:", odd_reversed)
'''



