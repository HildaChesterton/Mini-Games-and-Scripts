numbers = []

while True:
    user_input = input("Please enter a number (type Q to quit): ")
    if user_input.upper() == "Q":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except:
        print("Invalid input. Please enter a number or type Q to quit.")

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    average = sum(numbers) / len(numbers)
    max_number = max(numbers)
    min_number = min(numbers)
    print("Average of input numbers: ", average)
    print("Maximum of input numbers: ", max_number)
    print("Minimum of input numbers: ", min_number)
