def main():
    # Read student data from file
    with open("student_data.txt", "r") as file:
        lines = file.readlines()

    # Extract names and GWAs
    student_data = [line.strip().split() for line in lines]

    # Find maximum GWA
    max_gwa = max(float(student[1]) for student in student_data)

    # Find student(s) with maximum GWA
    top_students = [(student[0], float(student[1])) for student in student_data if float(student[1]) == max_gwa]

    # Output student(s) with highest GWA
    if len(top_students) == 1:
        print(f"The student with the highest GWA is: {top_students[0][0]} with a GWA of {top_students[0][1]}")
    else:
        print("The students with the highest GWA are:")
        for student in top_students:
            print(f"- {student[0]} with a GWA of {student[1]}")

if __name__ == "__main__":
    main()
