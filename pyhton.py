
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:

    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print(f"{number} is zero.")

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")