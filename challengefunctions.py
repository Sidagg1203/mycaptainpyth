def most_frequent(string):
    # Create an empty dictionary
    frequency = {}

    # Count the frequency of each letter in the string
    for letter in string:
        frequency[letter] = frequency.get(letter, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for item in sorted_frequency:
        print(item[0], "=", "{:02d}".format(item[1]))

# Prompt the user to enter a string
string = input("Please enter a string: ")

# Call the most_frequent function
most_frequent(string)
