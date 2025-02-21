from dataclasses import dataclass

@dataclass
class ErrorMontoInvalido(Exception):
    monto: int

    def __str__(self):
        return f"El monto de la compra no puede ser 0 o negativo. Monto ingresado: {self.monto}"