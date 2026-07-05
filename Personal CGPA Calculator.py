print("PERSONAL POCKET CGPA CALCULATOR")

courses = int(input("Enter number of courses: "))

total_points = 0
total_units = 0

for i in range(courses):
    print("\nCourse", i + 1)

    score = int(input("Enter score: "))
    unit = int(input("Enter course unit: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)
    print("Grade Point:", point)

    total_points += point * unit
    total_units += unit

cgpa = total_points / total_units

print("\n==========================")
print("Total Units:", total_units)
print("Total Grade Points:", total_points)
print("CGPA =", round(cgpa, 2))
print("==========================")
