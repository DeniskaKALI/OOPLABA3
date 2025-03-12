from __future__ import annotations
import json


class ComplexNumber:
 
    def __init__(self, real: float, imag: float) -> None:

        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    def __add__(self, other: ComplexNumber) -> ComplexNumber: # type: ignore
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber: # type: ignore
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber: # type: ignore
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber: # type: ignore
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ValueError("Деление на ноль невозможно.")
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    @classmethod
    def from_string(cls, str_value: str) -> ComplexNumber: # type: ignore
        parts = str_value.replace("i", "").split("+")
        real = float(parts[0].strip())
        imag = float(parts[1].strip()) if len(parts) > 1 else 0.0
        return cls(real, imag)

    def to_dict(self) -> dict:
        return {"real": self.real, "imag": self.imag}

    def save(self, filename: str) -> None:
        
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, filename: str) -> ComplexNumber: # type: ignore
        
        with open(filename, 'r') as f:
            data = json.load(f)
            return cls(data['real'], data['imag'])
