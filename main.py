class Pizza:
    def __init__(self, name: str, dough: str, sauce: str, toppings: list[str], price: float) -> None:
        self.name: str = name
        self.dough: str = dough
        self.sauce: str = sauce
        self.toppings: list[str] = toppings
        self.price: float = price

    def prepare(self) -> None:
        print(f'Готовим {self.name}: замес теста, добавление {self.sauce} и {", ".join(self.toppings)}.')

    def bake(self) -> None:
        print(f'Выпекаем {self.name}.')

    def cut(self) -> None:
        print(f'Режем {self.name}.')

    def pack(self) -> None:
        print(f'Упаковываем {self.name}.')

    def __str__(self) -> str:
        return f'{self.name} ({self.price} руб.)'

class PizzaPepperoni(Pizza):
    def __init__(self) -> None:
        super().__init__('Пепперони', 'тонкое', 'томатный', ['пепперони', 'сыр'], 500)

class PizzaBBQ(Pizza):
    def __init__(self) -> None:
        super().__init__('Барбекю', 'толстое', 'барбекю', ['курица', 'лук', 'сыр'], 600)

class PizzaSeafood(Pizza):
    def __init__(self) -> None:
        super().__init__('Дары Моря', 'тонкое', 'сливочный', ['креветки', 'мидии', 'сыр'], 700)

class Order:
    order_counter: int = 0
    
    def __init__(self) -> None:
        self.pizzas: list[Pizza] = []
        Order.order_counter += 1
        self.order_id: int = Order.order_counter
    
    def add_pizza(self, pizza: Pizza) -> None:
        self.pizzas.append(pizza)
        print(f'{pizza.name} добавлена в заказ.')
    
    def total_price(self) -> float:
        return sum(pizza.price for pizza in self.pizzas)
    
    def execute(self) -> None:
        print(f'Выполняем заказ #{self.order_id}')
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print(f'Заказ #{self.order_id} готов!')
    
    def __str__(self) -> str:
        return f'Заказ #{self.order_id}: ' + ', '.join(pizza.name for pizza in self.pizzas) + f' | Итог: {self.total_price()} руб.'

# Тестирование классов
# Тестирование создания пиццы
pizza1 = PizzaPepperoni()
print(pizza1)  # Ожидаемый результат: Пепперони (500 руб.)
    
pizza2 = PizzaBBQ()
print(pizza2)  # Ожидаемый результат: Барбекю (600 руб.)
    
# Тестирование заказа
order = Order()
order.add_pizza(pizza1)  # Ожидаемый результат: Пепперони добавлена в заказ.
order.add_pizza(pizza2)  # Ожидаемый результат: Барбекю добавлена в заказ.
    
print(order)  # Ожидаемый результат: Заказ #1: Пепперони, Барбекю | Итог: 1100 руб.
    
order.execute()  # Ожидаемый результат: последовательное выполнение методов prepare, bake, cut, pack
