with open("grades.txt", "w", encoding="utf-8") as f:
    f.write("John 90\n")
    f.write("Hannah 85\n")
    f.write("Hannah 95\n")
    f.write("Marry 78\n")
    f.write("John 75\n")
    f.write("Marry 82\n")

grades = {}

with open("grades.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, grade_str = line.strip().split()
        grade = int(grade_str)

        if name not in grades:
            grades[name] = []

        grades[name].append(grade)

with open("average_grades.txt", "w", encoding="utf-8") as f:
    for name, student_grades in grades.items():
        avg = sum(student_grades) / len(student_grades)
        f.write(f"{name} {avg:.2f}\n")
