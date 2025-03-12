import json
from complex_number import ComplexNumber

class ComplexCollection:
    """
    Класс-контейнер для хранения и управления набором комплексных чисел.
    """
    def __init__(self) -> None:
        #Инициализация контейнера
        self._data = []

    def __str__(self) -> str:
        #Строковое представление контейнера.
        return ", ".join(str(num) for num in self._data)

    def __getitem__(self, index: int) -> ComplexNumber:
        #Позволяет индексировать элементы контейнера.
        return self._data[index]

    def add(self, value: ComplexNumber) -> None:
        #Добавляет комплексное число в контейнер.
        self._data.append(value)

    def remove(self, index: int) -> None:
        #Удаляет комплексное число по индексу.
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс выходит за границы списка")

    def save(self, filename: str) -> None:
        #Сохраняет контейнер в JSON-файл.
        with open(filename, 'w') as f:
            json.dump([num.to_dict() for num in self._data], f)

    @classmethod
    def load(cls, filename: str) -> "ComplexCollection":
        #Загружает контейнер из JSON-файла.
        with open(filename, 'r') as f:
            data = json.load(f)
            collection = cls()
            for item in data:
                collection.add(ComplexNumber(item['real'], item['imag']))
            return collection
