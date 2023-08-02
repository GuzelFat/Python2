import csv

from descriptors import WordsCapitalize, NumberRange


class Student:
    """Класс, хранящий Ф.И.О., названия предметов, оценки и результаты тестов.\n
    Экземпляр класса сообщает средний балл по тестам для каждого предмета
    и по оценкам всех предметов вместе взятых."""
    _last_name = WordsCapitalize()
    _name = WordsCapitalize()
    _patronymic = WordsCapitalize()
    _grades = NumberRange(2, 5)
    _test_results = NumberRange(0, 100)

    def __init__(self, last_name: str, name: str, patronymic: str, file_name: str):
        self._last_name = last_name
        self._name = name
        self._patronymic = patronymic
        self._file_name = file_name
        self._subjects = self._subjects_from_scv()

    def __repr__(self):
        return f"Student('{self._last_name}', '{self._name}', '{self._patronymic}', '{self._file_name}')"

    @property
    def full_name(self):
        return f'{self._last_name} {self._name} {self._patronymic}'

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        if len(value) == 3:
            if value[0].capitalize() in self._subjects.keys():
                subj, grades, test_results = value
                if isinstance(grades, int):
                    self._grades = grades
                else:
                    for item in grades:
                        self._grades = item

                if isinstance(test_results, int):
                    self._test_results = test_results
                else:
                    for item in test_results:
                        self._test_results = item

                self._subjects.update({subj.capitalize():
                                       {'Оценки': grades if isinstance(grades, list)
                                        else [grades],
                                        'Результаты тестов': test_results if isinstance(test_results, list)
                                        else [test_results]}})
            else:
                print(f'Предмета {value[0]} нет у этого студента!')
        else:
            print('Неверное количество аргументов!')

    def _subjects_from_scv(self):
        """Метод, возвращающий словарь предметов из файла *.csv"""
        with open(self._file_name, encoding='utf-8') as file:
            csv_data = csv.DictReader(file, dialect='excel-tab', lineterminator='\n')
            subjects_list = [subject[0] for subject in csv_data.reader][1:]
            results = {subject: {'Оценки': [], 'Результаты тестов': []} for subject in subjects_list}
        return results

    def average_grade_results(self):
        """Метод, возвращающий словарь со средними оценками и средними результатами тестов для каждого предмета"""
        res = {}
        print('Средний балл по оценкам / тестам для каждого предмета:')
        for key, items in self._subjects.items():
            res.update({key: f'{sum(items.get("Оценки")) / len(items.get("Оценки"))} / '
                             f'{sum(items.get("Результаты тестов")) / len(items.get("Результаты тестов"))}'})
        return res

    def print_grade(self):
        """Метод печати общей успеваемости студента"""
        print(f'Успеваемость студента {self.full_name}:')
        for item in self._subjects.items():
            print(item)
        print()