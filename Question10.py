import math
import random
# Dictionary to store history
history = {}
result = 0
while True:
    # Display menu
    print("\n~~~~~ Smart Calculator ~~~~~")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")
    choice = input("Enter your choice: ")
    # Basic Arithmetic
    if choice == "1":
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            op = input("Enter Operator (+, -, *, /): ")
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                print("Invalid Operator")
                continue
            print("Result =", result)
        except:
            print("Invalid Input")
    # Scientific Calculation
    elif choice == "2":
        try:
            print("\n1. Square Root")
            print("2. Power")
            print("3. Factorial")
            ch = input("Enter Choice: ")
            if ch == "1":
                num = float(input("Enter Number: "))
                result = math.sqrt(num)
            elif ch == "2":
                base = float(input("Enter Base: "))
                power = float(input("Enter Power: "))
                result = math.pow(base, power)
            elif ch == "3":
                num = int(input("Enter Number: "))
                result = math.factorial(num)
            else:
                print("Invalid Choice")
                continue
            print("Result =", result)
        except:
            print("Invalid Input")
    # Generate Random Number
    elif choice == "3":
        result = random.randint(1, 100)
        print("Random Number =", result)
    # Store Result
    elif choice == "4":
        time = input("Enter Timestamp: ")
        history[time] = result
        print("Result Stored Successfully")
    # View History
    elif choice == "5":
        if len(history) == 0:
            print("No History Found")
        else:
            print("\nStored Results")
            for key, value in history.items():
                print(key, ":", value)
    # Exit
    elif choice == "6":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")