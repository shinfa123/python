# Lambda function to find the area of a square
area_of_square = lambda side: side ** 2

# Lambda function to find the area of a rectangle
area_of_rectangle = lambda length, width: length * width

# Lambda function to find the area of a triangle
area_of_triangle = lambda base, height: 0.5 * base * height

# Test the functions
side = 5
length = 10
width = 4
base = 6
height = 8

print("Area of square:", area_of_square(side))
print("Area of rectangle:", area_of_rectangle(length, width))
print("Area of triangle:", area_of_triangle(base, height))

