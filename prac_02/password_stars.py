min_length = 8  # Example minimum length
password = input("Enter password: ")

while len(password) < min_length:
    print("Error: Password is too short.")
    password = input("Enter password: ")

print("Success: Password accepted.")