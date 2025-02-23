# list_exercises.py

def main():
    # Prompt the user for 5 numbers and store them in a list
    numbers = []

    for i in range(5):
        number = int(input(f"Number {i + 1}: "))
        numbers.append(number)

    # Output information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

    # List of authorized usernames
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    # Ask for the user's username
    username = input("Enter your username: ")

    # Check if the username is in the authorized list
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
