class WordsCapitalize:
    """Дескриптор для проверки слова на наличие только букв и первую заглавную букву"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        """Валидатор, проверяющий слово на наличие только букв и первую заглавную букву"""
        if not value.isalpha():
            raise TypeError(f'Параметры ФИО должны состоять только из букв!')
        if not value.istitle():
            raise ValueError(f'В параметрах ФИО первая буква должна быть большой!')


class NumberRange:
    """Проверка вхождения числа в диапазон"""

    def __init__(self, min_num: int = None, max_num: int = None):
        self._min_num = min_num
        self._max_num = max_num

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Валидатор, проверяющий вхождение числа в диапазон"""
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self._min_num is not None and value < self._min_num or self._max_num is not None and value > self._max_num:
            raise ValueError(f'Значение {value} должно быть в диапазоне от {self._min_num} до {self._max_num}')