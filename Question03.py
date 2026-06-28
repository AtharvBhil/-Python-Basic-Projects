def manage_marks():
    marks = []
    # Take 5 subject marks
    while len(marks) < 5:
        try:
            mark = float(input("Enter mark: "))
            marks.append(mark)
        except ValueError:
            print("Please enter numbers only.")
    # Calculate average
    average = sum(marks) / len(marks)
    print("Average:", average)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    # Sort in descending order
    marks.sort(reverse=True)
    print("Sorted Marks:", marks)
manage_marks()