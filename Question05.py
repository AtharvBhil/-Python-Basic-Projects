def student_database():
    # Dictionary to store student records
    students = {}
    while True:
        print("\n~~~~~ Student Database ~~~~~")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter your choice: ")
        # Add student
        if choice == "1":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                # Add data using update()
                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student added successfully.")
            except ValueError:
                print("Invalid input! Roll number and age must be numbers.")
        # Search student
        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number to Search: "))
                # Search using get()
                student = students.get(roll)
                if student:
                    print("\nStudent Found")
                    print("Name :", student["Name"])
                    print("Age  :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found.")
            except ValueError:
                print("Please enter a valid roll number.")
        # Display all students
        elif choice == "3":
            if len(students) == 0:
                print("No student records available.")
            else:
                print("\nAll Student Records")
                for roll, data in students.items():
                    print("------------------------")
                    print("Roll Number :", roll)
                    print("Name        :", data["Name"])
                    print("Age         :", data["Age"])
                    print("City        :", data["City"])
        # Exit program
        elif choice == "4":
            print("Exiting Program...")
            break
        # Invalid menu choice
        else:
            print("Invalid choice! Please select between 1 and 4.")
# Function call
student_database()