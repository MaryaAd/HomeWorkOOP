class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_tw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_rating(self):
        grades_count = 0
        for course in self.grades:
            grades_count += len(self.grades[course])
        average_rating = sum(map(sum, self.grades.values())) / grades_count
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\n' \
              f'Средняя оценка за домашние задания: {round(self.av_rating(), 2)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение недопустимо')
            return
        return self.av_rating() < other.av_rating()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        grades_count = 0
        for course in self.grades:
            grades_count += len(self.grades[course])
        average_rating = sum(map(sum, self.grades.values())) / grades_count
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.av_rating(), 2)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение недопустимо')
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# лекторы
lecturer_1 = Lecturer('Ivan', 'Denisov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Petr', 'Sergeev')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python']

# проверяющие
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Oslo', 'Brend')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

# студенты
student_1 = Student('Denis', 'Sviridov', 'men')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.add_courses('Введение в программирование')

student_2 = Student('Roman', 'Malikov', 'men')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.add_courses('Введение в программирование')

# оценки лекторам
student_1.rate_tw(lecturer_1, 'Python', 10)
student_1.rate_tw(lecturer_1, 'Python', 10)
student_1.rate_tw(lecturer_1, 'Python', 10)

student_1.rate_tw(lecturer_2, 'Python', 5)
student_1.rate_tw(lecturer_2, 'Python', 7)
student_1.rate_tw(lecturer_2, 'Python', 8)

student_2.rate_tw(lecturer_1, 'Python', 7)
student_2.rate_tw(lecturer_1, 'Python', 8)
student_2.rate_tw(lecturer_1, 'Python', 9)

student_2.rate_tw(lecturer_2, 'Git', 10)
student_2.rate_tw(lecturer_2, 'Git', 8)
student_2.rate_tw(lecturer_2, 'Git', 9)

# оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 6)

reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)

reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 2)


print('Студенты, проходящие обучение:')
print(student_1)
print()
print(student_2)
print()
print(f'По результатам сравнения средних оценок студентов: \n'
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname}\n'
      f'Итог: {student_1 > student_2}')
print()
print("Лекторы:")
print(lecturer_1)
print()
print(lecturer_2)
print()
print(f'По результатам сравнения средних оценок лекторов: \n'
      f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname}\n'
      f'Итог: {lecturer_1 > lecturer_2}')
print()
print("Проверяющие:")
print(reviewer_1)
print()
print(reviewer_2)
print()

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def student_average_grade_on_the_course(student_list, course):
    all_average_grade = []
    for stud in student_list:
        all_average_grade.extend(stud.grades.get(course, []))
    if not all_average_grade:
        return 'По данному курсу оценки не проставлены'
    return round(sum(all_average_grade) / len(all_average_grade), 2)


def lecturer_average_grade_on_the_course(lecturer_list, course):
    all_average_grade = []
    for lect in lecturer_list:
        all_average_grade.extend(lect.grades.get(course, []))
    if not all_average_grade:
        return 'По данному курсу оценки не проставлены'
    return round(sum(all_average_grade) / len(all_average_grade), 2)


print(f"Средняя оценка для всех студентов по курсу {'Python'}:"
      f" {student_average_grade_on_the_course(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех студентов по курсу {'Git'}: "
      f"{student_average_grade_on_the_course(student_list, 'Git')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}:"
      f" {lecturer_average_grade_on_the_course(lecturer_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Git'}:"
      f" {lecturer_average_grade_on_the_course(lecturer_list, 'Git')}")
print()