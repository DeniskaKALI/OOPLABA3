from abc import ABC, abstractmethod

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
