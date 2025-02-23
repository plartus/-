class Vehicle:
    """Базовый класс транспорта."""
    def __init__(self, brand: str, model: str, year: int):
        """Конструктор базового класса."""
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        :return: Строка с описанием транспортного средства.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        :return: Строка, которую можно использовать для создания объекта.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

    def start_engine(self) -> str:
        """
        Запуск двигателя транспортного средства.
        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель {self.brand} {self.model} запущен."


class Car(Vehicle):
    """Дочерний класс легкового транспорта."""
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, mileage: int = 0):
        """Конструктор дочернего класса."""
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self._mileage = mileage  # Инкапсулированный атрибут, чтобы предотвратить прямое изменение пробега.

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для добавления информации о типе топлива.
        :return: Строка с описанием автомобиля.
        """
        return f"{super().__str__()}, Тип топлива: {self.fuel_type}, Пробег: {self._mileage} км"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для добавления информации о типе топлива и пробеге.
        :return: Формальное строковое представление объекта.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, fuel_type={self.fuel_type!r}, mileage={self._mileage!r})"

    def start_engine(self) -> str:
        """
        Перегрузка метода start_engine для добавления информации о типе топлива.
        :return: Сообщение о запуске двигателя с указанием типа топлива.
        """
        return f"Двигатель {self.brand} {self.model} ({self.fuel_type}) запущен."

    def drive(self, distance: int) -> str:
        """
        Метод для возможности увеличения пробега автомобиля.
        :param distance: Расстояние, на которое проехал автомобиль.
        :return: Сообщение о новом пробеге.
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        self._mileage += distance
        return f"Пробег {self.brand} {self.model} увеличен на {distance} км. Текущий пробег: {self._mileage} км."

    @property
    def mileage(self) -> int:
        """
        Свойство для получения текущего пробега.
        :return: Текущий пробег автомобиля.
        """
        return self._mileage


if __name__ == "__main__":
    # Создаю объект базового класса
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    print(vehicle)  # Toyota Corolla (2020)
    print(repr(vehicle))  # Vehicle(brand='Toyota', model='Corolla', year=2020)
    print(vehicle.start_engine())  # Двигатель Toyota Corolla запущен.

    # Создаю объект дочернего класса
    car = Car("Tesla", "Model S", 2022, "электро", 15000)
    print(car)  # Tesla Model S (2022), Тип топлива: электро, Пробег: 15000 км
    print(repr(car))  # Car(brand='Tesla', model='Model S', year=2022, fuel_type='электро', mileage=15000)
    print(car.start_engine())  # Двигатель Tesla Model S (электро) запущен.
    print(car.drive(100))  # Пробег Tesla Model S увеличен на 100 км. Текущий пробег: 15100 км.
    print(f"Текущий пробег: {car.mileage} км")  # Текущий пробег: 15100 км
    pass
