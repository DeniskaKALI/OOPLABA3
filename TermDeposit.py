
from BankDeposit import BankDeposit

class TermDeposit(BankDeposit):
    def calculate_profit(self) -> float:
        return self.principal * self.annual_rate * self.term_in_years