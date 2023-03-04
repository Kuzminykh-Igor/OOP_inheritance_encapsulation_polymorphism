class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Метод оценки лектора"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.grades = {}


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        """Метод оценки студентов"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Игорь', 'Кузьминых', 'м')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Вася', 'Пупкин', 'м')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Компьютерная грамотность']

reviever_1 = Reviewer('Брюс', 'Беннер')
reviever_1.courses_attached += ['Python']

reviever_1.rate_hw(student_1, 'Python', 8)
reviever_1.rate_hw(student_1, 'Python', 9)
reviever_1.rate_hw(student_1, 'Python', 10)

reviever_1.rate_hw(student_2, 'Python', 6)
reviever_1.rate_hw(student_2, 'Python', 7)
reviever_1.rate_hw(student_2, 'Python', 8)

reviever_2 = Reviewer('Тони', 'Старк')
reviever_2.courses_attached += ['Git']

reviever_2.rate_hw(student_1, 'Git', 7)
reviever_2.rate_hw(student_1, 'Git', 8)
reviever_2.rate_hw(student_1, 'Git', 9)

reviever_2.rate_hw(student_2, 'Git', 5)
reviever_2.rate_hw(student_2, 'Git', 6)
reviever_2.rate_hw(student_2, 'Git', 7)

lecturer_1 = Lecturer('Олег', 'Булыгин', 'Python')
lecturer_2 = Lecturer('Алёна', 'Батицкая', 'Git')

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 7)

print(student_1.grades)
print(student_2.grades)
print(lecturer_1.grades)
print(lecturer_2.grades)