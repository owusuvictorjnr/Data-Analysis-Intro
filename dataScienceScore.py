import csv

students = [
    ("John Doe", 25,80),
    ("Jane Doe", 20,91),
    ("Mary Smith", 22,66),
    ("Peter Jones", 28,60),
    ("Susan Brown", 18,55),
    ("David Green", 18,50),
    ("Emily White", 30,77),
    ("Michael Black", 30,70),
    ("Sarah Blue", 30,89),
    ("William Red", 17,49),
]


# Open a CSV file in write mode
with open("data_science_students.csv", "w") as csvfile:

     # Create a CSV writer object
    csvwriter = csv.writer(csvfile, delimiter=",")


      # Write the header row
    csvwriter.writerow(["name", "midsemScore", "examScore", ])


      # Write the student data
    for student in students:
        csvwriter.writerow(student)


# Calculate the average exam score
average_exam_score = sum(student[2] for student in students) / len(students)

# Find the maximum exam score
maximum_exam_score = max(student[2] for student in students)

# Find the minimum exam score
minimum_exam_score = min(student[2] for student in students)

print("The average exam score is", average_exam_score)
print("The maximum exam score is", maximum_exam_score)
print("The minimum exam score is", minimum_exam_score)
