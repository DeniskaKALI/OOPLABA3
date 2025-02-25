Лабораторная работа №3 
Выполнил Островерхов Денис Юрьевич ПИЖ-б-о-23-1

# Проект "Римские числа" с принципами ООП

Этот проект демонстрирует работу с римскими числами с использованием основных принципов объектно-ориентированного программирования (ООП): абстракции, наследования, инкапсуляции, полиморфизма и композиции. В проекте реализованы следующие классы:

- **NumberBase** — абстрактный базовый класс, определяющий интерфейс для работы с числами.
- **Roman** — класс для работы с римскими числами, реализующий все методы из NumberBase.
- **TArray** — класс, который хранит список объектов типа Roman и умеет суммировать их.

---

## Классы и их методы

### NumberBase (Абстрактный класс)
Определяет интерфейс для числовых классов. В него включены следующие абстрактные методы, которые должны быть реализованы в наследниках:

- **to_int() -> int**  
  Преобразует число в целое число.

- **to_roman() -> str**  
  Преобразует число в строку, содержащую римское представление.

- **__call__() -> int**  
  Позволяет вызывать объект как функцию и возвращать его целочисленное значение.

- **__add__(other: NumberBase) -> NumberBase**  
  Метод для сложения чисел.

- **__sub__(other: NumberBase) -> NumberBase**  
  Метод для вычитания чисел.

- **__mul__(other: NumberBase) -> NumberBase**  
  Метод для умножения чисел.

- **__truediv__(other: NumberBase) -> NumberBase**  
  Метод для деления чисел (целочисленное деление).

- **__str__() -> str**  
  Метод для получения строкового представления числа (обычно римской записи).

---

### Roman (Класс для работы с римскими числами)
Реализует все методы, объявленные в абстрактном классе NumberBase. Позволяет выполнять арифметические операции, конвертацию между римскими и арабскими числами и вызывать объект как функцию.

#### Конструктор
- **Roman(value: int | str)**  
  Принимает целое число или строку с римским числом. Если передано число, оно сохраняется напрямую, а если строка – происходит преобразование в целое число. Значение должно быть больше нуля.

#### Методы
- **to_int() -> int**  
  Возвращает внутреннее целочисленное представление числа.

- **to_roman() -> str**  
  Возвращает строковое римское представление числа.

- **__call__() -> int**  
  Позволяет вызывать объект как функцию. При вызове возвращает целочисленное значение.

- **__add__(other: Roman) -> Roman**  
  Складывает два объекта типа Roman и возвращает новый объект с суммой.

- **__sub__(other: Roman) -> Roman**  
  Вычитает одно число из другого. Если результат меньше 1, выбрасывается ошибка.

- **__mul__(other: Roman) -> Roman**  
  Умножает два объекта Roman и возвращает новый объект с произведением.

- **__truediv__(other: Roman) -> Roman**  
  Делит одно число на другое (используется целочисленное деление). Если делитель равен нулю или результат меньше 1, выбрасывается ошибка.

- **__str__() -> str**  
  Возвращает строковое представление числа (римскую запись), что удобно при выводе объекта через `print()`.

#### Статические методы
- **roman_to_int(roman_str: str) -> int**  
  Преобразует строку с римским числом в целое число.

- **int_to_roman(number: int) -> str**  
  Преобразует целое число в строку с римским представлением.

---

### TArray (Класс для работы с массивом римских чисел)
Демонстрирует принцип композиции. Хранит список объектов Roman и умеет выполнять агрегирующую операцию (суммирование).

#### Конструктор
- **TArray(values: List[int | str])**  
  Принимает список чисел или строк (римских чисел) и преобразует каждый элемент в объект Roman.

#### Методы
- **__call__() -> Roman**  
  Позволяет вызывать объект TArray как функцию. При вызове суммирует все элементы массива с помощью метода `__add__` класса Roman и возвращает объект Roman с суммой.

- **__str__() -> str**  
  Возвращает строковое представление массива, где каждый элемент выводится в виде римской записи.

---
