groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "marks": [5, 5, 5]
    }
]

def filter_students_by_avg(students, min_avg):
    result = []
    for student in students:
        marks = student["marks"]
        avg = sum(marks) / float(len(marks))
        if avg >= min_avg:
            result.append(student)
    return result

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(12),
          "Оценки".ljust(20), "Средний балл")
    for student in students:
        marks = student["marks"]
        avg = sum(marks) / float(len(marks))
        marks_str = ", ".join(str(m) for m in marks)
        print(
            student["name"].ljust(15),
            student["surname"].ljust(12),
            marks_str.ljust(20),
            f"{avg:.2f}"
        )

while True:
    user_input = input("\nВведите минимальный средний балл: ").strip()
    min_avg = float(user_input)
    filtered = filter_students_by_avg(groupmates, min_avg)

    if filtered:
        print(f"\nСтуденты со средним баллом {min_avg}:")
        print_students(filtered)
    else:
        print(f"\nНет студентов со средним баллом {min_avg}.")
