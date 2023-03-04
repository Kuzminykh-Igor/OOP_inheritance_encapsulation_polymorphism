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

    def __average_grades(self):
        """Метод считает среднюю оценку за все домашние задания"""
        res = []
        for grade in self.grades.values():
            res.extend(grade)
        return round(sum(res) / len(res), 2)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__average_grades()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершённые курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        """Метод сравнения студентов по средней оценке за все домашние задания"""
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average_grades() < other.__average_grades()


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

    def __average_grades(self):
        """Метод считает среднюю оценку за все лекции"""
        res = []
        for grade in self.grades.values():
            res.extend(grade)
        return round(sum(res) / len(res), 2)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.__average_grades()}'

    def __lt__(self, other):
        """Метод сравнения лекторов по средней оценке за все лекции"""
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_grades() < other.__average_grades()


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

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


student_1 = Student('Игорь', 'Кузьминых', 'м')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Компьютерная грамотность']
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

reviever_1.rate_hw(student_2, 'Python', 7)
reviever_1.rate_hw(student_2, 'Python', 7)
reviever_1.rate_hw(student_2, 'Python', 8)

reviever_2 = Reviewer('Тони', 'Старк')
reviever_2.courses_attached += ['Git']

reviever_2.rate_hw(student_1, 'Git', 8)
reviever_2.rate_hw(student_1, 'Git', 8)
reviever_2.rate_hw(student_1, 'Git', 9)

reviever_2.rate_hw(student_2, 'Git', 7)
reviever_2.rate_hw(student_2, 'Git', 6)
reviever_2.rate_hw(student_2, 'Git', 7)

lecturer_1 = Lecturer('Олег', 'Булыгин', 'Python')
lecturer_2 = Lecturer('Алёна', 'Батицкая', 'Git')

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 8)


print('Ревьюеры:\n')
print(reviever_1, '\n')
print(reviever_2, '\n')

print('Лекторы:\n')
print(lecturer_1, '\n')
print(lecturer_2, '\n')
print(f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname}:', lecturer_1 < lecturer_2)
print(f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname}:', lecturer_1 > lecturer_2, '\n')

print('Студенты:\n')
print(student_1, '\n')
print(student_2, '\n')
print(f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname}:', student_1 < student_2)
print(f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname}:', student_1 > student_2, '\n')
