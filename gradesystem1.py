header1 = "STUDENT'S GRADING SYSTEM"
header2 = "COMPUTER SCIENCE      2025  SEMESTER ONE"
print(header1.center(100))
print(header2.center(100))

sur_name = input("Enter your Surname: ")
first_name = input("Enter your first name: ")
reg_number = input("\nRegistration number: ")

print(f"\nStudent {sur_name} {first_name} with registration number: {reg_number}\n")


numberOfCourseUnits = int(input("How many course units do you have: "))
counter = 1
sum_CreditHours = 0
sum_GradePoints = 0
while counter <= numberOfCourseUnits:
    course_unit = input(f"\nENTER COURSE UNIT {counter}: ")
    score = int(input(f"\nPercentage marks for {course_unit}: "))
    
    CreditHours = float(input(f"Enter the credit hours for {course_unit}: "))

    GradePointValue = (score/100) * 5
    GradePoint = CreditHours * GradePointValue

    
    if (GradePointValue > 5.0 or GradePointValue < 0.0):
        print("Invalid mark entered")
        exit(0)
    else:
        print(f"The grade for {course_unit} basing on the grade point value is: ", end=' ')
        if (GradePointValue >= 4.4):
            print("A+")
            
        elif(GradePointValue >= 4.0):
            print("A")
            
        elif(GradePointValue >= 3.5):
            print("B+")

        elif (GradePointValue >= 3.0):
            print("B")
            
        elif (GradePointValue >= 2.5):
            print("C+")

        elif (GradePointValue >= 2.0):
            print("C")

        elif (GradePointValue >= 1.5):
            print("D+")

        elif (GradePointValue >= 1.0):
            print("D")

        else:
            print("F")

    print(f"The Grade Point Course in {course_unit} is {GradePoint}, congratulations")
    sum_CreditHours += CreditHours
    sum_GradePoints += GradePoint
    counter += 1
    
    
    
GradePointAverage = round(sum_GradePoints / sum_CreditHours, 1)
print(f"The GPA of {sur_name} {first_name} in all course units is {GradePointAverage}, congratulations")
    