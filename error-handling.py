## Task 1 - Understanding Python Exceptions

while True:
    try:
        number = input("Enter a number: ")
        value = float(number)
        result = 100 / value
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
        continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue
    else:
        print(f"100 divided by {value} is {result}.")
        break
## Task 2 - Types of Exceptions

list_example = [1, 2, 3]
dict_example = {'a': 1, 'b': 2}
str_example = "Hello"
int_example = 5
# Try to access an invalid list index
try:
    print(list_example[5])  # This will raise IndexError because the index 5 is out of range for the list.
except IndexError as e:
    print("IndexError occurred! List index out of range.", e)
# Try to access a non-existent key in a dictionary
try:
    print(dict_example['c'])  # This will raise KeyError because 'c' is not a key in the dictionary.
except KeyError as e:
    print("KeyError occurred! Key not found in the dictionary.", e)
# Try to add a string and an integer
try:
    result = str_example + int_example  # This will raise TypeError because you cannot add a string and an integer.
except TypeError as e:
    print("TypeError occurred! Unsupported operand types.", e)

# Task 3 - Using try...except...else...finally
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

try:
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter numeric values.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
