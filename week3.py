# TASK 1 done
# Write a Python function that receives a list of numbers. The function should use for loop or while loop to return a subset of the original list that contains members meeting the criteria below:
# • The number should be odd and divisible by 5.
# OR
# • The number should be negative and divisible by 7.
# You may use this list for testing: numbers = [5, 10, 15, -7, -14, 20, -21, 35, 40, -49, 55, 63, 23, -8, 19, -82]


'''

def filter_numbers(numbers):
    
    result = []
    for num in numbers:
# Check first condition: odd and divisible by 5
        if (num % 2 != 0 and num % 5 == 0) or (num < 0 and num % 7 == 0):
            result.append(num)
    return result

# Example usage
numbers = [5, 10, 15, -7, -14, 20, -21, 35, 40, -49, 55, 63, 23, -8, 19, -82]
filtered_list = filter_numbers(numbers)
print("Filtered numbers:", filtered_list)
'''
    
# TASK 2  done
# Repeat the above task without the use any conventional loop in python.


'''
def filter_numbers_recursive(numbers):
   
    # Base case: if the list is empty, return an empty list
    if not numbers:
        return []
    
    # Process the first element
    first = numbers[0]

    # Check if the first element meets either condition
    if (first % 2 != 0 and first % 5 == 0) or (first < 0 and first % 7 == 0):
        # Include this number and continue recursively with the rest of the list
        return [first] + filter_numbers_recursive(numbers[1:])
    else:
        # Skip this number and continue recursively with the rest of the list
        return filter_numbers_recursive(numbers[1:])
    
# Example usage
numbers = [5, 10, 15, -7, -14, 20, -21, 35, 40, -49, 55, 63]
filtered_list = filter_numbers_recursive(numbers)
print("Filtered numbers (recursive):", filtered_list)
'''

# TASK 3 done
# Write a Python function that opens a text file, reads its content, and creates a list containing only the numbers that appear in the file. The function should ignore any non-numeric data and return the list of numbers.

'''
def extract_numbers_from_file(filename):
    numbers = []
    try:
        # Open the file safely
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into parts based on spaces
                parts = line.strip().split()

                for part in parts:
                    # Check if the part is a valid number
                    try:
                        # Convert to integer if possible, otherwise float
                        if ',' in part:
                            numbers.append(float(part.replace(',', '.')))
                        else:
                            numbers.append(int(part))
                    except ValueError:
                        # Ignore parts that are not numbers
                        continue
        return numbers
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# opcje wywolania
# 1:
nums = extract_numbers_from_file("/home/monik/Pulpit/mtu/data_analytics/AnimalFarm.txt")
print(nums)

# 2:
filename = "/home/monik/Pulpit/mtu/data_analytics/AnimalFarm.txt"
result = extract_numbers_from_file(filename)
print("Numbers extracted from file:", result)
'''

# TASK 4 done
# Write a Python program that reads all files in a given folder and creates a dictionary where the keys are the filenames and the values are the number of words in each file.

'''
import os

def count_words_in_folder(folder_path):

    word_counts = {}

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Process only text files
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    words = content.split()  # Split by whitespace
                    # save without extension
                    name_without_ext = os.path.splitext(filename)[0]
                    word_counts[name_without_ext] = len(words)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return word_counts


# Example usage
folder = "/home/monik/Pulpit/mtu/data_analytics"  # Replace with your folder path
result = count_words_in_folder(folder)
print(result)
'''

# TASK 5 done
# he Fibonacci numbers form the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1. Each subsequent number is the sum of the two preceding numbers. Create a program that prints the first 40 Fibonacci numbers.


'''
# My version
fibonacci_numbers = [0, 1]
for i in range(2,40):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(fibonacci_numbers)
'''

'''
def fibonacci_40():
    a, b = 0, 1

    print("The first 40 Fibonacci numbers: ")

    for _ in range(40):
        print(a, end=" ")
        a, b = b, a + b
fibonacci_40()
'''

# TASK 6
# Repeat the above task, this time, create a Python program that generates the first 40 Fibonacci numbers and stores them in a dictionary.
# The key of the dictionary should represent the index (position) of the Fibonacci number, starting from 0.
# The value should be the Fibonacci number at that position.Once the dictionary is created, the program should print all key-value pairs in a clear format, showing the index alongside its corresponding Fibonacci number.

'''
def fibonacci_dict(n):
    """
Generate the first n Fibonacci numbers and store them in a dictionary.
Key = index (starting at 0)
Value = Fibonacci number
"""
    fib_dict = {}
    a, b = 0, 1
    for i in range(n):
        fib_dict[i] = a # Store the Fibonacci number with its index
        a, b = b, a + b # Update to the next numbers
    return fib_dict
# Generate and print the first 40 Fibonacci numbers
fib_sequence = fibonacci_dict(40)
print("Fibonacci sequence (index: value):")
for index, value in fib_sequence.items():
    print(f"{index}: {value}")
'''

# TASK 7
# Write a function that receives two dictionaries, merges them, and prints the unique values from the merged dictionary. Explain what happens if the two input dictionaries contain one or more items with the same key

'''
def dictionary_merge(n1, n2):
    n1.update(n2)
    # Note that update function does not return anything, instead it updates n1.
    print(n1)
    uniques = set(n1.values())
    print(uniques)

h1 = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
h2 = {'e': 1, 'f': 20, 'g': 2, 'd': 30}

dictionary_merge(h1, h2)
'''


# TASK 8
#  restaurant system requires a safe interaction between two entities within the software. The first entity is responsible for generating a collection of food items along with their prices.
# This collection should then be sent to the second entity. The second entity is responsible for preparing the bill for the ordered food but must not be able to modify the original prices.
# Write two functions, each representing one of these entities, ensuring that all the above con- ditions are met.

'''
def generate_menu():
    """
    First entity: Generates a collection of food items with their prices.
    Returns the menu as an immutable tuple of tuples to prevent modification.
    """
    menu_items = (
        ("Pizza", 12.99),
        ("Burger", 8.49),
        ("Pasta", 10.99),
        ("Salad", 6.50),
        ("Soup", 4.75)
    )
    return menu_items


def prepare_bill(menu, order):
    """
    Second entity: Prepares the bill for the customer.
    It cannot modify the original menu because the menu is immutable.

    Parameters:
    - menu (tuple): The menu received from the first entity.
    - order (list): List of dish names ordered by the customer.
    """
    print("\n---- Generating Bill ----")
    total = 0.0
    # Convert menu to a dictionary for easy lookup
    menu_dict = dict(menu)
    for dish in order:
        if dish in menu_dict:
            price = menu_dict[dish]
            print(f"{dish}: ${price:.2f}")
            total += price
        else:
            print(f"{dish}: Not available")
    print("-" * 25)
    print(f"Total: ${total:.2f}")


# --- Main Program Simulation ---

# First entity generates the menu
restaurant_menu = generate_menu()

# Display menu
print("---- Restaurant Menu ----")
for dish, price in restaurant_menu:
    print(f"{dish}: ${price:.2f}")

# Simulate a customer order
customer_order = ["Pizza", "Soup", "Burger"]

# Second entity prepares the bill
prepare_bill(restaurant_menu, customer_order)

# Attempt to change a price (this should fail to demonstrate safety)
try:
    restaurant_menu[0] = ("Pasta", 20.00)
except TypeError as e:
    print("\nError: Cannot modify menu data!")
    print("Reason:", e)
'''