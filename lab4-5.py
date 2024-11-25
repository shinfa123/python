# Function to add variable-length integer arguments
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Test the function
result = add_numbers(10, 20, 30, 40, 50)  # You can pass any number of integers here
print("The sum is:", result)

