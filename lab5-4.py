# generate_armstrongs.py

from armstrong import is_armstrong_number

def generate_armstrong_numbers(start, end):
    """
    Generate all Armstrong numbers between two limits, inclusive.
    """
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Example usage:
if __name__ == "__main__":
    start = int(input("Enter the starting limit: "))
    end = int(input("Enter the ending limit: "))
    
    armstrong_numbers = generate_armstrong_numbers(start, end)
    
    print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")



