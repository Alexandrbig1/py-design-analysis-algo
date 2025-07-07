class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    assigned_teachers = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = 0

        for teacher in teachers:
            available_subjects = teacher.can_teach_subjects & remaining_subjects
            if len(available_subjects) > best_coverage or (
                    len(available_subjects) == best_coverage and best_teacher and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                best_coverage = len(available_subjects)

        if not best_teacher:
            return None  # Impossible to cover all subjects

        best_teacher.assigned_subjects = best_teacher.can_teach_subjects & remaining_subjects
        remaining_subjects -= best_teacher.assigned_subjects
        assigned_teachers.append(best_teacher)

    return assigned_teachers


if __name__ == '__main__':
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}

    teachers = [
        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Mathematics", "Physics"}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher("Serhii", "Kovalenko", 50, "s.kovalenko@example.com", {"Informatics", "Mathematics"}),
        Teacher("Nataliia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Informatics"}),
        Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Class schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")