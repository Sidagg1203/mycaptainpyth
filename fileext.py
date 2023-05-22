def get_file_extension(filename):
    # Split the filename by the dot
    parts = filename.split('.')
    return parts[-1]

# Accept filename from the user
filename = input("Enter a filename: ")

# Get the file extension
extension = get_file_extension(filename)

# Print the extension
print("The extension of the file is:", extension)