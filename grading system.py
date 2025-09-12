header1 = "STUDENT'S GRADING SYSTEM"
header2 = "COMPUTER SCIENCE      2025  SEMESTER ONE"
print(header1.center(100))
print(header2.center(100))

name = input("Enter your name: ")
reg_number = input("\nRegistration number: ")

print(f"\nStudent {name} with registration number: {reg_number}\n")


numberOfCourseUnits = int(input("How many course units do you have "))
counter = 1

while counter <= numberOfCourseUnits:
    course_unit = input(f"\nENTER COURSE UNIT {counter}: ")
    score = int(input("Marks: "))

    if (score > 100 or score < 0):
        print("Invalid score entered")
        exit(0)
    else:
        print(f"The grade for {course_unit} is: ", end=' ')
        if (score >= 80):
            print("A")
            
        elif(score >= 75):
            print("B+")

        elif (score >= 70):
            print("B")
            
        elif (score >= 65):
            print("C+")

        elif (score >= 60):
            print("C")

        elif (score >= 55):
            print("D+")

        elif (score >= 50):
            print("D")

        else:
            print("F")

    print("")
    
    counter += 1