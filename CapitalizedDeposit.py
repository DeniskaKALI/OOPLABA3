from BankDeposit import BankDeposit

class CapitalizedDeposit(BankDeposit):
    """
    Вклад с капитализацией процентов (сложные проценты).
    """
    def calculate_profit(self) -> float:
        return self.principal * ((1 + self.annual_rate) ** self.term_in_years - 1)
    