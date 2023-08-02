"""Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""
from student_cls import Student

if __name__ == '__main__':
    student_first = Student('Иванов', 'Андрей', 'Иванович', 'student1.csv')
    print(student_first.full_name)
    student_first.print_grade()
    student_first.subjects = 'Математика', 5, 70
    student_first.print_grade()
    student_first.subjects = 'Английский язык', 5, 85
    student_first.print_grade()
    student_first.subjects = 'Математика', [4, 3, 5, 5], [0, 86, 92, 58]
    student_first.subjects = 'Биология', [3, 4, 3, 3], [33, 45, 18]
    student_first.subjects = 'Химия', [3, 4, 5, 3], 46
    student_first.subjects = 'Русский язык', 2, [71, 28]
    student_first.print_grade()
    print(student_first.average_grade_results())