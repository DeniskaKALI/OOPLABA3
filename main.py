from TermDeposit import TermDeposit
from BonusDeposit import BonusDeposit
from CapitalizedDeposit import CapitalizedDeposit
from Reccomend import recommend_deposit

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

deposit = recommend_deposit(150_000.0, 0.1, 2)
print(f"Рекомендованный вклад: {deposit}")
print(f"Ожидаемая прибыль: {deposit.calculate_profit():.2f}")
# Ожидаемый результат:
# Тип вклада: CapitalizedDeposit (principal=100000, rate=0.1, term=3)
# Ожидаемая прибыль: 33100.00 (100000 * ((1 + 0.1)^3 - 1))