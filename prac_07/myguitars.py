from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w') as file:
        file.write("Name,Year,Cost\n")
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost:.1f}\n"
            file.write(line)


def display_guitars(guitars):
    """Display a list of Guitar objects."""
    for index, guitar in enumerate(guitars, 1):
        print(f"{index}. {guitar}")


def get_new_guitars():
    """Prompt the user to enter new guitars and return a list of Guitar objects."""
    guitars = []
    print("Enter your new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")
    return guitars


def main():
    """Main function to handle the guitar program workflow."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("\nOriginal guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    save_guitars(filename, guitars)
    print(f"\nSaved {len(guitars)} guitars to {filename}")


if __name__ == "__main__":
    main()