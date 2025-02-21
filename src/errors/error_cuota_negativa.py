from dataclasses import dataclass

@dataclass
class ErrorCuotaNegativa(Exception):
    numero_cuotas: int

    def __str__(self):
        return f"El numero de cuotas no puede ser 0 o negativo. Numero de cuotas ingresado: {self.numero_cuotas}"