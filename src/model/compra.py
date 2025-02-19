from dataclasses import dataclass

@dataclass
class Compra:
    monto: float
    numero_cuotas: int
    tasa_interes: float

    def calcular_cuota_mensual(self) -> float:
        pass

    def calcular_interes(self) -> float:
        pass