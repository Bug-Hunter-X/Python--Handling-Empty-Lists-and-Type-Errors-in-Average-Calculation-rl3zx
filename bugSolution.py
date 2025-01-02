def calculate_average(numbers):
    if not numbers:
        return 0
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List must contain only numbers.")
        return None

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_numbers_with_strings = [10, '20', 30]
average_mixed = calculate_average(my_numbers_with_strings) #This will now return an error message and None 