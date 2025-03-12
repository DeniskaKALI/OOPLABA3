from TermDeposit import TermDeposit

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
