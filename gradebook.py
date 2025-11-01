# Name: Muskan Kumari , Date: 30-10-2025, Title: Gradebook Management System
print("Welcome")
def calculate_avg(marks):   
    sum=0
    count=0
    for mark in marks.values():
        sum += mark
        count += 1
    avg = sum / count
    return avg

def calculate_median(marks):
    marks = sorted(marks.values())
    n = len(marks)
    mid = n // 2
    if n % 2 == 0:
        return (marks[mid - 1] + marks[mid]) / 2
    else:
        return marks[mid]

def max_marks(marks):
    return max(marks.values())      

def min_marks(marks):
    return min(marks.values())

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name of student: ")
        mark = int(input("Enter marks of student: "))  
        marks[name] = mark
    return marks 
def assign_grade(marks):
    grades = {}  
    for name, mark in marks.items():
        if mark >= 90:
            grades[name] = "A"
        elif 80 <= mark <= 89:
            grades[name] = "B"
        elif 70 <= mark <= 79:
            grades[name] = "C"
        elif 60 <= mark <= 69:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

marks = manual_input()
grades = assign_grade(marks)
average = calculate_avg(marks)
print("Average marks:", average)

median = calculate_median(marks)
print("Median:", median)

maxmarks = max_marks(marks)
print("Maximum marks:", maxmarks)

minmarks = min_marks(marks)
print("Minimum marks:", minmarks)


print("Grades:" , grades)



grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for grade in grades.values():
    grade_count[grade] += 1


print("\nGrade Distribution of Students:")
for grade, count in grade_count.items():
    print(f"Grade {grade} - {count} student{'s' if count != 1 else ''}")

passed_students=[]
failed_students=[]
for name, mark in marks.items():
    if mark >= 40:
        passed_students.append(name)
    else:
        failed_students.append(name)
print("\nNo. of students passed or failed:")
print(f"Number of students passed: {len(passed_students)}")
print("Passed students:", passed_students)

print(f"\nNumber of students failed: {len(failed_students)}")
print("Failed students:", failed_students)

print("\n=====Student Result Table=====")
print("Name\tMarks\tGrade")
print("==============================")
for name, mark in marks.items():
    grade=grades[name]
    print(f"{name}\t{mark}\t{grade}")