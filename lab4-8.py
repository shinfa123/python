# Function to calculate factorial of a number
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

# Function to calculate the sum of the series
def sum_series(n):
    series_sum = 0
    for i in range(1, n + 1):
        # For each term, we calculate i^3 / i!
        series_sum += (i ** 3) / factorial(i)
    return series_sum

# Input: number of terms in the series
n = int(input("Enter the value of n: "))

# Calculate the sum of the series
result = sum_series(n)

# Output the result
print(f"The sum of the series up to {n} terms is: {result}")

