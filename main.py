from complex_number import ComplexNumber
from complex_collection import ComplexCollection

def main():
    # Создание контейнера
    collection = ComplexCollection()

    # Добавление элементов
    collection.add(ComplexNumber(1, 2))
    collection.add(ComplexNumber(3, 4))
    collection.add(ComplexNumber(-1, -5))

    print("Контейнер после добавления элементов:")
    print(collection)

    # Индексация
    print("Первый элемент контейнера:", collection[0])

    # Удаление элемента
    collection.remove(1)
    print("Контейнер после удаления второго элемента:")
    print(collection)

    # Сохранение в JSON
    collection.save("complex_collection.json")

    # Загрузка из JSON
    loaded_collection = ComplexCollection.load("complex_collection.json")
    print("Загруженный контейнер:")
    print(loaded_collection)

if __name__ == "__main__":
    main()
