def read_wimbledon_data(filename):
    """Reads the Wimbledon data from the provided CSV file and returns the relevant information."""
    champions = []  # To store the champion names
    countries = []  # To store the countries of champions

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip header if present
        next(in_file)  # Uncomment this line if your CSV file has a header
        for line in in_file:
            data = line.strip().split(",")  # Split by commas for CSV format
            if len(data) > 4:  # Check if the line has the expected number of columns
                champions.append(data[2])  # Champion's name is in column 3
                countries.append(data[1])  # Champion's country is in column 2
                # Debug line to inspect the data
                print(f"Data: {data}")

    return champions, countries


def count_champions_wins(champions):
    """Returns a dictionary of champion names and their respective win counts."""
    wins = {}
    for champion in champions:
        if champion in wins:
            wins[champion] += 1
        else:
            wins[champion] = 1
    return wins


def list_countries(countries):
    """Returns a sorted list of unique countries."""
    unique_countries = set(countries)  # Use a set to ensure uniqueness
    return sorted(unique_countries)


def display_results(wins, countries):
    """Displays the champions' win counts and the sorted list of countries."""
    # Display champions and their win counts
    print("Wimbledon Champions: ")
    for champion, count in wins.items():
        print(f"{champion} {count}")

    # Display countries in alphabetical order
    print("\nThese countries have won Wimbledon: ")
    print(", ".join(countries))


def main():
    """Main function to orchestrate the reading, processing, and displaying of data."""
    filename = "wimbledon.csv"  # Path to the file (make sure this is correct)

    # Read and process the data
    champions, countries = read_wimbledon_data(filename)

    # Count champion wins
    wins = count_champions_wins(champions)

    # List and sort countries
    sorted_countries = list_countries(countries)

    # Display the results
    display_results(wins, sorted_countries)


if __name__ == "__main__":
    main()
