from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class BankDeposit(ABC):

    def __init__(self, principal: float, annual_rate: float, term_in_years: int) -> None:
        self.principal: float = principal
        self.annual_rate: float = annual_rate
        self.term_in_years: int = term_in_years

    @abstractmethod
    def calculate_profit(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (principal={self.principal}, rate={self.annual_rate}, term={self.term_in_years})"


class TermDeposit(BankDeposit):
    def calculate_profit(self) -> float:
        return self.principal * self.annual_rate * self.term_in_years


class BonusDeposit(TermDeposit):
    def __init__(
        self,
        principal: float,
        annual_rate: float,
        term_in_years: int,
        bonus_rate: float,
        threshold: float
    ) -> None:
        super().__init__(principal, annual_rate, term_in_years)
        self.bonus_rate: float = bonus_rate
        self.threshold: float = threshold

    def calculate_profit(self) -> float:
        base_profit = super().calculate_profit()  # используем формулу простых процентов
        if self.principal > self.threshold:
            base_profit += base_profit * self.bonus_rate
        return base_profit


class CapitalizedDeposit(BankDeposit):
    def calculate_profit(self) -> float:
        return self.principal * ((1 + self.annual_rate) ** self.term_in_years - 1)


def recommend_deposit(
    principal: float,
    annual_rate: float,
    term_in_years: int,
    threshold: float = 100_000.0,
    bonus_rate: float = 0.05
) -> BankDeposit:
    deposits: List[BankDeposit] = [
        TermDeposit(principal, annual_rate, term_in_years),
        BonusDeposit(principal, annual_rate, term_in_years, bonus_rate, threshold),
        CapitalizedDeposit(principal, annual_rate, term_in_years)
    ]

    # Сравниваем вклады по рассчитанной прибыли и возвращаем наиболее выгодный
    best_deposit = max(deposits, key=lambda d: d.calculate_profit())
    return best_deposit




# Пример 1: Срочный вклад (TermDeposit)
deposit1 = TermDeposit(100_000, 0.1, 3)
print(f"Тип вклада: {deposit1}")  
print(f"Ожидаемая прибыль: {deposit1.calculate_profit():.2f}")  
# Ожидаемый результат:
# Тип вклада: TermDeposit (principal=100000, rate=0.1, term=3)
# Ожидаемая прибыль: 30000.00

# Пример 2: Бонусный вклад (BonusDeposit) с превышением порога
deposit2 = BonusDeposit(150_000, 0.1, 3, bonus_rate=0.05, threshold=100_000)
print(f"Тип вклада: {deposit2}")  
print(f"Ожидаемая прибыль: {deposit2.calculate_profit():.2f}")  
# Ожидаемый результат:
# Тип вклада: BonusDeposit (principal=150000, rate=0.1, term=3)
# Ожидаемая прибыль: 47250.00 (т.к. 150000 * 0.1 * 3 = 45000 + 5% бонуса)

# Пример 3: Вклад с капитализацией (CapitalizedDeposit)
deposit3 = CapitalizedDeposit(100_000, 0.1, 3)
print(f"Тип вклада: {deposit3}")  
print(f"Ожидаемая прибыль: {deposit3.calculate_profit():.2f}")  
# Ожидаемый результат:
# Тип вклада: CapitalizedDeposit (principal=100000, rate=0.1, term=3)
# Ожидаемая прибыль: 33100.00 (100000 * ((1 + 0.1)^3 - 1))

# Пример 4: Рекомендация лучшего вклада
best_deposit = recommend_deposit(150_000, 0.1, 3)
print(f"Лучший вариант вклада: {best_deposit}")  
print(f"Максимальная ожидаемая прибыль: {best_deposit.calculate_profit():.2f}")  
# Ожидаемый результат:
# Лучший вариант вклада: CapitalizedDeposit (principal=150000, rate=0.1, term=3)
# Максимальная ожидаемая прибыль: 49650.00 (сложные проценты при капитализации)
