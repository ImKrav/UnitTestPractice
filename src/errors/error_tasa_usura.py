from dataclasses import dataclass

@dataclass
class ErrorTasaUsura(Exception):
    tasa_interes: float

    def __str__(self):
        return f"La tasa de interes {self.tasa_interes} supera la tasa de usura"