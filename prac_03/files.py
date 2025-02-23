# 1
# Ask for the user's name and write it to the file
name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()
#2
# Read the name from the file and print a greeting
file = open('name.txt', 'r')
name = file.read().strip()  # Using strip() to remove any unwanted newline
file.close()
print(f"Hi {name}!")
#3
# Read the first two numbers from the file and add them together
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    result = num1 + num2
    print(result)  # Should output 59
#4
# Calculate the total for all numbers in the file
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())  # Strip to remove newline and convert to int
    print(total)  # Prints the sum of all numbers
