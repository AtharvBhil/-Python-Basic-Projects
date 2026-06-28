# Lambda function for square
square = lambda x: x * x
try:
    numbers = list(range(1, 21))
    squares = []
    # Store squares
    for i in numbers:
        squares.append(square(i))
    print("Even Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num)
except Exception as e:
    print("Error:", e)