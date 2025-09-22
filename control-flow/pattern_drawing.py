# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Print newline after each row
    print()
    row += 1
