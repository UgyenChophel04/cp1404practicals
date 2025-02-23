"""
CP1404/CP5632 Practical
Data file -> lists program
"""
# subject_reader.py

FILENAME = "subject_data.txt"  # Ensure this file exists in the same directory

def load_data():
    """Reads the subject data from file and returns a list of lists."""
    subject_data = []  # List to store all the subject information

    try:
        with open(FILENAME, 'r') as input_file:
            for line in input_file:
                line = line.strip()  # Remove any trailing whitespace
                parts = line.split(',')  # Split by comma to separate subject, lecturer, students

                # Convert the number of students to an integer
                try:
                    parts[2] = int(parts[2])
                except ValueError:
                    print(f"Error: Unable to convert the number of students in line: {line}")
                    continue

                # Append the parts as a list to the subject_data list
                subject_data.append(parts)

    except FileNotFoundError:
        print(f"Error: File '{FILENAME}' not found.")
        return []

    return subject_data  # Return the list of lists
