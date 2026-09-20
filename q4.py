import random

# Generate a list of 5 random floating-point numbers
numbers = [random.uniform(0, 10) for _ in range(5)]

# Display the generated numbers
print("Random numbers:")

for number in numbers:
    print(number)

# Find the minimum and maximum values
minimum = min(numbers)
maximum = max(numbers)

# Display the results
print("Minimum value:", minimum)
print("Maximum value:", maximum)

Random numbers:
3.45
8.72
1.26
6.91
4.38

Minimum value: 1.26
Maximum value: 8.72
