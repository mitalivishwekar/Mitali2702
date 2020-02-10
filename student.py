class Student:

    def __init__(self, name, rollno, MarkMaths, MarkEnglish, MarkScience):
        self.name = name
        self.rollno = rollno
        self.MarkMaths = MarkMaths
        self.MarkEnglish = MarkEnglish
        self.MarkScience = MarkScience

    def display(self):

        print("name:", self.name)
        print("rollno:", self.rollno)

    def Enter_Marks(self):
        print("MarkMaths:", self.MarkMaths)
        print("MarkEnglish:", self.MarkEnglish)
        print("MarkScience:", self.MarkScience)

    def total_Marks(self, MarkMaths, MarkEnglish, MarkScience):
        self.total_Marks = (MarkMaths + MarkEnglish + MarkScience)
        self.Percentage = (self.total_Marks) * 100 / 300
        print("Total marks: ", self.total_Marks)
        print("Percentage:", self.Percentage)
        if (self.Percentage >= 75):
            print("The Grade Obtain Is: A+")
        elif (self.Percentage >= 35):
            print("The Grade Obtain Is: B")
        else:
            print("The Grade Obtain Is: F")
name = input("Please enter your name: ")
rollno = input("Please enter your rollno: ")
MarkMaths = int(input("Enter the Maths Marks:"))
MarkEnglish = int(input("Enter the English Marks:"))
MarkScience = int(input("Enter the Science Marks:"))

S1 = Student(name, rollno, MarkMaths, MarkEnglish, MarkScience)
S1.display()
S1.Enter_Marks()
S1.total_Marks(MarkMaths, MarkEnglish, MarkScience)
