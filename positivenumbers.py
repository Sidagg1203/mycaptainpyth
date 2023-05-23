numbers = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in numbers]
for num in numbers:
    if num > 0:
        print(num)





