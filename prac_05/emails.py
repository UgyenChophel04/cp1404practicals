"""
Email and Name Storage
Estimate: 25 minutes
Actual:   30 minutes
"""


# Function to extract the name from the email (before '@')
def extract_name_from_email(email):
    name_part = email.split('@')[0]
    # Capitalize the first letter of each part of the name
    name = ' '.join([word.title() for word in name_part.split('.')])
    return name


# Dictionary to store email to name mapping
email_to_name = {}

# Loop to get user emails and names
while True:
    email = input("Email: ").strip()

    # Exit loop when email is blank
    if email == "":
        break

    name = extract_name_from_email(email)

    # Ask for confirmation of the name
    confirmation = input(f"Is your name {name}? (Y/n): ").strip().lower()

    if confirmation != "" and confirmation != "y":
        # If the user enters anything other than Y or presses Enter (which defaults to Y)
        name = input("Name: ").strip()

    # Store the email and name in the dictionary
    email_to_name[email] = name

# Loop through dictionary and print all stored emails and names
print("\nStored users:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
