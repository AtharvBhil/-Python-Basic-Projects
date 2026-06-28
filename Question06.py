import random
import math
try:
    numbers = set()
    # Take 10 numbers
    while len(numbers) < 10:
        num = int(input("Enter Number: "))
        numbers.add(num)
    # Convert set into tuple
    data = tuple(numbers)
    print("Tuple:", data)
    # Pick 3 random numbers
    print("Random Numbers:", random.sample(data, 3))
    # Find square root
    total = sum(data)
    print("Square Root:", math.sqrt(total))
except Exception as e:
    print("Error:", e)