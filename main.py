from abc import ABC, abstractmethod
from typing import List, Union

# Абстрактный базовый класс, в котором объявлены все методы, используемые в классе Roman.
class NumberBase(ABC):
    @abstractmethod
    def to_int(self) -> int:
        pass

    @abstractmethod
    def to_roman(self) -> str:
        pass

    @abstractmethod
    def __call__(self) -> int:
        pass

    @abstractmethod
    def __add__(self, other: 'NumberBase') -> 'NumberBase':
        pass

    @abstractmethod
    def __sub__(self, other: 'NumberBase') -> 'NumberBase':
        pass

    @abstractmethod
    def __mul__(self, other: 'NumberBase') -> 'NumberBase':
        pass

    @abstractmethod
    def __truediv__(self, other: 'NumberBase') -> 'NumberBase':
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# Класс Roman: реализует преобразование между int и римской записью, арифметические операции и метод __call__
class Roman(NumberBase):
    def __init__(self, value: Union[int, str]) -> None:
        if isinstance(value, int):
            self.__value = value
        else:
            self.__value = self.roman_to_int(value)

    def to_int(self) -> int:
        # Возвращает число в виде int
        return self.__value

    def to_roman(self) -> str:
        # Возвращает число в виде римской записи
        return self.int_to_roman(self.__value)

    def __add__(self, other: 'Roman') -> 'Roman':
        # Складывает два римских числа и возвращает новый объект Roman
        return Roman(self.__value + other.to_int())

    def __sub__(self, other: 'Roman') -> 'Roman':
        # Вычитает два римских числа, если результат меньше 1 – ошибка
        new_val = self.__value - other.to_int()
        if new_val < 1:
            raise ValueError("Result must be > 0.")
        return Roman(new_val)

    def __mul__(self, other: 'Roman') -> 'Roman':
        # Умножает два римских числа
        return Roman(self.__value * other.to_int())

    def __truediv__(self, other: 'Roman') -> 'Roman':
        # Делит два римских числа (целочисленное деление)
        if other.to_int() == 0:
            raise ZeroDivisionError("Division by zero.")
        new_val = self.__value // other.to_int()
        if new_val < 1:
            raise ValueError("Result must be > 0.")
        return Roman(new_val)

    @staticmethod
    def roman_to_int(roman_str: str) -> int:
        # Преобразует римскую строку в целое число
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for ch in reversed(roman_str):
            value = roman_map.get(ch, 0)
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total

    @staticmethod
    def int_to_roman(number: int) -> str:
        # Преобразует целое число в римскую запись
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = []
        for arabic, roman_sym in roman_numerals:
            while number >= arabic:
                result.append(roman_sym)
                number -= arabic
        return "".join(result)

    def __str__(self) -> str:
        # Метод для получения строкового представления объекта
        return self.to_roman()
    
    def __call__(self) -> int:
        # При вызове объекта возвращает число в виде int
        return self.__value

# Класс TArray: хранит список объектов Roman и реализует метод __call__ для суммирования элементов
class TArray:
    def __init__(self, values: List[Union[int, str]]) -> None:
        # Преобразует каждый элемент списка в объект Roman
        self._items = [Roman(v) for v in values]

    def __call__(self) -> Roman:
        # При вызове объекта суммирует все элементы и возвращает объект Roman с результатом
        if not self._items:
            raise ValueError("Empty array.")
        total = self._items[0]
        for item in self._items[1:]:
            total = total + item
        return total

    def __str__(self) -> str:
        # Возвращает строковое представление массива: римские записи всех элементов
        return "[" + ", ".join(item.to_roman() for item in self._items) + "]"

# Пример использования с комментариями результата каждого метода

# Создаем массив объектов Roman из чисел [3, 1, 4, 1, 5, 9]
arr = TArray([3, 1, 4, 1, 5, 9])
print("Исходный массив:", arr)
# Результат работы __str__ TArray:
# Вывод: Исходный массив: [III, I, IV, I, V, IX]

# Вызов TArray как функции (метод __call__) для получения суммы элементов
total_roman = arr()
print("Сумма элементов (римскими):", total_roman)
# Результат работы __call__ TArray и __add__ Roman:
# Сумма: 3 + 1 + 4 + 1 + 5 + 9 = 23, римской записью: XXIII

# Вызов объекта Roman как функции (метод __call__) для получения целочисленного значения
print("Сумма элементов (целое число):", total_roman())
# Результат работы __call__ Roman:
# Вывод: 23

# Демонстрация арифметических операций с римскими числами
r1 = Roman("X")  # "X" = 10
r2 = Roman("V")  # "V" = 5

sum_result = r1 + r2
print("X + V =", sum_result)
# Результат работы __add__:
# 10 + 5 = 15, римской записью: XV

sub_result = r1 - r2
print("X - V =", sub_result)
# Результат работы __sub__:
# 10 - 5 = 5, римской записью: V

mul_result = r1 * r2
print("X * V =", mul_result)
# Результат работы __mul__:
# 10 * 5 = 50, римской записью: L

div_result = r1 / r2
print("X / V =", div_result)
# Результат работы __truediv__:
# 10 // 5 = 2, римской записью: II
