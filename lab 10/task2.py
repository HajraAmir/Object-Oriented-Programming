import csv

persons_data = [
    ("HAJRA", "USA", "Female", 28.5, "hajra is kind-hearted and intelligent."),
    ("SIDRA", "Canada", "Female", 35.2, "sidra is hardworking and creative."),
    ("RABIA", "UK", "Female", 42.8, "rabia is adventurous and compassionate.")
]
with open('idealized_persons.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Nationality", "Gender", "Age", "Notes"])
    writer.writerows(persons_data)
with open('idealized_persons.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        name, nationality, gender, age, notes = row
        print("Name:", name)
        print("Nationality:", nationality)
        print("Gender:", gender)
        print("Age:", age)
        print("Notes:", notes)
        print()