# List of exponents (0, 1, 2, ..., n)
n = 10  # You can change this to any number to get powers of 2 up to 2^n

# Use map with lambda to calculate powers of 2
powers_of_2 = list(map(lambda x: 2 ** x, range(n+1)))

# Display the result
print(powers_of_2)

