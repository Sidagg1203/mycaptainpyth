myList = [0, 1]  # Initialize the sequence with the first two numbers
n = int(input("Enter the number of Fibonacci numbers to generate: "))

    # Generate the Fibonacci sequence
for i in range(2, n):
    next_number = myList[i - 1] + myList[i - 2]
    myList.append(next_number)

print(myList)
