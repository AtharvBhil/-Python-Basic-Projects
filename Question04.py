class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    # Add marks
    def add_mark(self, mark):

        if 0 <= mark <= 100:
            self.marks_list.append(mark)
        else:
            print("Invalid Marks")
    # Calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    # Display student details
    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
student = Student(name, roll)
for i in range(5):
    try:
        mark = float(input("Enter Mark: "))
        student.add_mark(mark)
    except ValueError:
        print("Invalid Input")
student.display_info()