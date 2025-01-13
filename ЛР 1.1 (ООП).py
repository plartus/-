# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Student:
    def __init__(self, name: str, grades: list):
        """
        Создание объекта "Студент"

        :param name: Имя студента
        :param grades: Список оценок студента

        Примеры:
        >>> student = Student("Иван", [5, 4, 3, 5])  # инициализация студента
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError("Все оценки должны быть числами")
        if not isinstance(grades, list):
            raise TypeError("Оценки должны быть в виде списка")
        self.grades = grades

    def add_grade(self, grade: float) -> None:
        """
        Добавление оценки студенту.

        :param grade: Оценка, которую нужно добавить

        Примеры:
        >>> student = Student("Иван", [5, 4, 3])
        >>> student.add_grade(5)
        >>> student.grades
        [5, 4, 3, 5]
        """
        if not isinstance(grade, int):
            raise TypeError("Оценка должна быть числом")
        self.grades.append(grade)

    def average_grade(self) -> float:
        """
        Вычисление средней оценки студента.

        :return: Средняя оценка

        Примеры:
        >>> student = Student("Иван", [5, 4, 3, 5])
        >>> student.average_grade()
        4.25
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


class Bowl:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Миска"

        :param capacity_volume: Объем миски
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> bowl = Bowl(1000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем миски должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем миски должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bowl(self) -> bool:
        """
        Функция, которая проверяет является ли миска пустой

        :return: Является ли миска пустой

        Примеры:
        >>> bowl = Bowl(1000, 0)
        >>> bowl.is_empty_bowl()
        True
        """
        return self.occupied_volume == 0

    def add_water_to_bowl(self, water: float) -> None:
        """
        Добавление воды в миску.

        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в миске, то вызываем ошибку

        Примеры:
        >>> bowl = Bowl(1000, 0)
        >>> bowl.add_water_to_bowl(300)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError("Не хватает свободного места в миске")
        self.occupied_volume += water


class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        """
        Создание объекта "Книга"

        :param title: Заголовок книги
        :param author: Автор книги
        :param publication_year: Год публикации книги

        Примеры:
        >>> book = Book("Сияние", "Стивен Кинг", 1977)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        self.author = author

        if not isinstance(publication_year, int):
            raise TypeError("Год публикации должен быть целым числом")
        if publication_year < 0:
            raise ValueError("Год публикации не может быть отрицательным")
        self.publication_year = publication_year

    def get_info(self) -> str:
        """
        Получение информации о книге.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("Сияние", "Стивен Кинг", 1977)
        >>> book.get_info()
        'Сияние, Стивен Кинг, 1977'
        """
        return f"{self.title}, {self.author}, {self.publication_year}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest
