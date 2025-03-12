from typing import List
from TermDeposit import TermDeposit
from BonusDeposit import BonusDeposit
from CapitalizedDeposit import CapitalizedDeposit
from BankDeposit import BankDeposit

def recommend_deposit(principal: float, annual_rate: float, term_in_years: int, threshold: float = 100_000.0, bonus_rate: float = 0.05) -> BankDeposit:
    """
    Рекомендует вклад с максимальной прибылью.
    """
    deposits: List[BankDeposit] = [ # type: ignore
        TermDeposit(principal, annual_rate, term_in_years),
        BonusDeposit(principal, annual_rate, term_in_years, bonus_rate, threshold),
        CapitalizedDeposit(principal, annual_rate, term_in_years)
    ]
    return max(deposits, key=lambda d: d.calculate_profit())
